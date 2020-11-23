import socket
import argparse
import os
from time import sleep

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
numPacketsToSend      = 10

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="client.py", description="client to send udp traffic")
    parser.add_argument('packetsRate', type=int, help='how many packets are sent each cycle towards the udp server')
    parser.add_argument('totalPackets', type=int, help='how many total packets are sent towards the udp server')
    args = parser.parse_args()

    rate = args.packetsRate
    numPacketsToSend = args.totalPackets
    
    print("send {} packets with {} packets/sec").format(numPacketsToSend, rate)
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    i = 0
    while i < numPacketsToSend:
        for j in range (rate):
            # Send to server using created UDP socket
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msg = "Message received from Server: {}".format(msgFromServer[0])
        print("sent {} messages".format(rate))
        i = i + rate
        sleep(1)
        