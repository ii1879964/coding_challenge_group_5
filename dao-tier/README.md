Here will be the dao-tier image & code

Step 1: Run server

see database/README.md

Step 2: Install requirements (for fist time)

`pip install -r dao-tier/requirements.txt`

Step 3: Execute commands

Examples:

- connection check:

`curl localhost:8090/connection_check -X GET`

- login check with login and password parameters:

`curl -d "{\"login\":\"debs\", \"password\":\"gradprog2016@02\"}" -H "Content-Type: application/json" -X post localhost:8090/login_check`

- view all deals history:

`curl -X get localhost:8090/deals/history`

- view all deals for specific instrument (f.e. Eclipse): 

`curl -X get localhost:8090/deals/history/Eclipse`

- runtime deals:

`curl -X get localhost:8090/deals/stream`

- view average prices (suy and sell) for all instruments:
 
`curl -X get localhost:8090/instruments/average_price`

- view all instruments:

`curl -X get localhost:8090/instruments`

- view total quantity for all instruments:

`curl -X get localhost:8090/instruments/ending_position`

