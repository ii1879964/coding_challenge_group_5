import mysql.connector
from instruments_dao import InstrumentsDAO

instruments_dao = InstrumentsDAO(host='localhost',
                                 database='db_grad_test',
                                 user='root',
                                 password='ppp',
                                 port=3307)


def test_get_instruments_names():
    test_instruments = ['InstrumentA', 'InstrumentB', 'InstrumentC']
    result = instruments_dao.get_all_instrument_names()
    assert set(test_instruments) == set(result), "Instruments isn't the same"



def test_get_instrument_average_prices():
    result = instruments_dao.get_all_instrument_average_prices()

    test_average_price= [
        {
            "name": 'InstrumentA',
            "prices":
                 {
                    "buy": 800.0,
                    "sell": 200.0
                 }
        },
        {
            "name": 'InstrumentB',
            "prices":
                {
                    "buy": 100.0,
                    "sell": 0.0
                }
        },
        {
            "name": 'InstrumentC',
            "prices":
                {
                    "buy": 0.0,
                    "sell": 0.0
                }
        }
    ]

    assert len(result) == len(test_average_price), "Dictionaries have different length"
    for instrument_price in result:
        instrument_name = instrument_price['name']
        found = 0
        for test_price in test_average_price:
            if test_price['name'] == instrument_name:
                price = instrument_price['prices']['sell']
                assert test_price['prices']['sell'] == instrument_price['prices']['sell'], "Buy price isn't the same"
                assert test_price['prices']['buy'] == instrument_price['prices']['buy'], "Sell price isn't the same"
                found += 1
        assert found != 0, "Instrument don't found"

# if __name__ == '__main__':
#     test_get_instruments_names()
