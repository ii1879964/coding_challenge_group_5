import mysql


class ProbesDAO(object):
    def __init__(self,
                 host='localhost',
                 database='db_grad_cs_1917',
                 user='root',
                 password='ppp'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def check_connection(self):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            return True if conn.is_connected() else False
        finally:
            conn.close()

    def check_login(self, login, password):
        try:
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM users where user_id='{login}' and user_pwd='{password}'")
            cursor.fetchall()
            return True if cursor.rowcount == 1 else False
        finally:
            cursor.close()
            conn.close()
