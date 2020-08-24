Command for running SQL container:

`docker run  -v %cd%/database/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 --rm -e MYS
QL_ROOT_PASSWORD=ppp mysql:latest
`