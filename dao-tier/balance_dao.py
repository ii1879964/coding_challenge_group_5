import mysql


class BalanceDAO(object):

    balance_per_instrument_name = {}
    quantity_of_shares = {}
    current_price = {}

    def get_realized_balance():
        return sum(BalanceDAO.balance_per_instrument_name.values())

    def get_effective_balance():
        effective_balance = 0
        for instrument, balance in BalanceDAO.balance_per_instrument_name.items():
            effective_balance += balance + BalanceDAO.current_price[instrument] * BalanceDAO.quantity_of_shares[instrument]
        return effective_balance

    def recount_profit_loss(new_deal):
        if not new_deal['instrumentName'] in BalanceDAO.quantity_of_shares:
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] = 0
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] = 0

        if (new_deal['type'] == 'B'):
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] -= new_deal['quantity'] * new_deal['price']
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] += new_deal['quantity']
            BalanceDAO.current_price[new_deal['instrumentName']] = new_deal['price']
        else:
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] += new_deal['quantity'] * new_deal['price']
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] -= new_deal['quantity']
            BalanceDAO.current_price[new_deal['instrumentName']] = new_deal['price']


