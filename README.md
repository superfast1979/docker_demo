# docker_demo
Simple interaction between microservices into docker containers

This demo uses some docker containers:

- simple udp client written in python (not in docker container)
- container app with a simple udp server written in python
- container db with mariadb database
- container webapp with a simple flask http server
- container cache with redis nosql db

The purpose is the container's interactions orchestrated with docker-compose and docker containers.
The udp client send udp packets to the container app.
The container app save info into mariadb container.
The webapp shows a simple gui and query the mariadb, also cache the requested queries into redis to lower latency response.

