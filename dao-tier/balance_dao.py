import mysql


class BalanceDAO(object):

    balance_per_instrument_name = {}
    quantity_of_shares = {}
    current_price = {}

    @staticmethod
    def get_realized_balance():
        result = {"profit":0,"loss":0,"sum":0}
        for v in BalanceDAO.balance_per_instrument_name.values():
            if v >= 0:
                result['profit'] += v
            else:
                result['loss'] -= v
        result['sum'] = result['profit'] - result['loss']
        return result

    @staticmethod
    def get_effective_balance():
        result = {"profit": 0, "loss": 0, "sum": 0}
        for instrument, balance in BalanceDAO.balance_per_instrument_name.items():
            if balance >= 0:
                result['profit'] += balance
            else:
                result['loss'] -= balance
            if BalanceDAO.quantity_of_shares[instrument] >= 0:
                result['profit'] += BalanceDAO.current_price[instrument] * BalanceDAO.quantity_of_shares[instrument]
            else:
                result['loss'] -= BalanceDAO.current_price[instrument] * BalanceDAO.quantity_of_shares[instrument]
        result['sum'] = result['profit'] - result['loss']
        return result

    @staticmethod
    def recount_profit_loss(new_deal):
        if not new_deal['instrumentName'] in BalanceDAO.quantity_of_shares:
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] = 0
        if not new_deal['instrumentName'] in BalanceDAO.balance_per_instrument_name:
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] = 0

        if (new_deal['type'] == 'B'):
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] -= new_deal['quantity'] * new_deal['price']
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] += new_deal['quantity']
            BalanceDAO.current_price[new_deal['instrumentName']] = new_deal['price']
        else:
            BalanceDAO.balance_per_instrument_name[new_deal['instrumentName']] += new_deal['quantity'] * new_deal['price']
            BalanceDAO.quantity_of_shares[new_deal['instrumentName']] -= new_deal['quantity']
            BalanceDAO.current_price[new_deal['instrumentName']] = new_deal['price']


