Command for running SQL container:

`docker run  -v %cd%/database/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 --rm -e MYSQL_ROOT_PASSWORD=ppp mysql:latest
`

Restart server or fix "Port is already allocated":

1. `docker ps`

2. `docker kill *CONTAINER ID*`

3. `docker run -v %cd%/database/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 --rm -e MYSQL_ROOT_PASSWORD=ppp mysql:latest`