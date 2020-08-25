import mysql


class InstrumentsDAO(object):
    def __init__(self,
                 host='localhost',
                 database='db_grad_cs_1917',
                 user='root',
                 password='ppp',
                 port='3306'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def get_all_instrument_names(self):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT instrument_name FROM instrument")
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def get_all_instrument_average_prices(self):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "instrument_name, "
                "deal_type, "
                "avg(deal_price) "
                "FROM "
                "deal join "
                "instrument on deal.deal_instrument_id=instrument.instrument_id "
                "GROUP BY "
                "instrument_name,"
                "deal_type "
                "HAVING "
                "instrument_name IN (SELECT instrument_name FROM instrument)")
            instrument_prices = {}
            for row in cursor.fetchall():
                if row[0] not in instrument_prices:
                    instrument_prices[row[0]] = {"B": 0, "S": 0}
                instrument_prices[row[0]][row[1]] = row[2]
            return [
                {
                    "name": name,
                    "prices":
                        {
                            "buy": prices["B"],
                            "sell": prices["S"]
                        }
                 }
                for name, prices in instrument_prices.items()]
        finally:
            cursor.close()
            conn.close()


    def get_all_instrument_ending_positions(self):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "instrument_name, "
                "deal_type, "
                "sum(deal_quantity) "
                "FROM "
                "deal join "
                "instrument on deal.deal_instrument_id=instrument.instrument_id "
                "GROUP BY "
                "instrument_name,"
                "deal_type "
                "HAVING "
                "instrument_name IN (SELECT instrument_name FROM instrument)")
            instrument_positions = {}
            for row in cursor.fetchall():
                if row[0] not in instrument_positions:
                    instrument_positions[row[0]] = {"B": 0, "S": 0}
                instrument_positions[row[0]][row[1]] = row[2]
            return [
                {
                    "name": name,
                    "prices":
                        {
                            "buy": positions["B"],
                            "sell": positions["S"]
                        }
                }
                for name, positions in instrument_positions.items()]
        finally:
            cursor.close()
            conn.close()
