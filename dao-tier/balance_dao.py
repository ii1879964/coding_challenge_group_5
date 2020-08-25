import mysql


class BalanceDAO(object):

    balance_per_instrument_name = {}
    qunatity_of_shares = {}
    current_price = {}
    def __init__(self,
                 host='localhost',
                 database='db_grad_cs_1917',
                 user='root',
                 password='ppp'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_realized_balance(self):
        return sum(BalanceDAO.balance_per_instrument_name.values())

    def get_effective_balance(self):
        effective_balance = 0
        for instrument, balance in BalanceDAO.balance_per_instrument_name.items():
            effective_balance += balance + BalanceDAO.current_price[instrument] * BalanceDAO.qunatity_of_shares[instrument]
        return effective_balance

    def recount_profit_loss(self, new_deal):
        if not new_deal['instrument_name'] in BalanceDAO.qunatity_of_shares:
            BalanceDAO.qunatity_of_shares[new_deal['instrument_name']] = 0
            BalanceDAO.balance_per_instrument_name[new_deal['instrument_name']] = 0

        if (new_deal['type'] == 'B'):
            BalanceDAO.balance_per_instrument_name[new_deal['instrument_name']] -= new_deal['qunatity'] * new_deal['price']
            BalanceDAO.qunatity_of_shares[new_deal['instrument_name']] -= new_deal['qunatity']
            BalanceDAO.current_price[new_deal['instrument_name']] = new_deal['price']
        else:
            BalanceDAO.balance_per_instrument_name[new_deal['instrument_name']] += new_deal['qunatity'] * new_deal['price']
            BalanceDAO.qunatity_of_shares[new_deal['instrument_name']] += new_deal['qunatity']
            BalanceDAO.current_price[new_deal['instrument_name']] = new_deal['price']


