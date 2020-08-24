Command for running SQL container:

`docker run  -v %cd%/database/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 --rm -e MYSQL_ROOT_PASSWORD=ppp mysql:latest
`

If port is already allocated in first launch:

`docker ps`

`docker kill *CONTAINER ID*`