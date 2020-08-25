import mysql


class DealsDAO(object):
    def __init__(self,
                 host='localhost',
                 database='db_grad_cs_1917',
                 user='root',
                 password='ppp'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_all_deals(self):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "deal_time,"
                "instrument_name,"
                "counterparty_name,"
                "deal_type,"
                "deal_quantity,"
                "deal_price "
                "FROM "
                "deal join "
                "instrument  on deal.deal_instrument_id=instrument.instrument_id join "
                "counterparty on deal.deal_counterparty_id=counterparty.counterparty_id")
            return [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()

    def filter_deals_by_instrument(self, instrument):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "deal_time,"
                "instrument_name,"
                "counterparty_name,"
                "deal_type,"
                "deal_quantity,"
                "deal_price "
                "FROM "
                "deal join "
                "instrument  on deal.deal_instrument_id=instrument.instrument_id join "
                "counterparty on deal.deal_counterparty_id=counterparty.counterparty_id "
                "WHERE "
                f"instrument_name='{instrument}'")
            return [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()
