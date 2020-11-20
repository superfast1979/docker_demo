# docker_demo
Simple interaction between microservices into docker containers

This demo uses some docker containers:

- simple udp client written in python (not in docker container)
- container app with a simple udp server written in python
- container db with mariadb database
- container webapp with a simple flask http server

The purpose is the container's interactions orchestrated with docker-compose and docker containers.
The udp client send udp packets to the container app.
The container app save info into mariadb container.
The webapp shows a simple gui and query the mariadb to count inserted record

# Install

After installing docker and docker-compose go to root source directory and type:
docker-compose build
docker-compose up -d
docker-compose logs
