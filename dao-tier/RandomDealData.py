import time
import numpy, random
from datetime import datetime, timedelta
import json
from Instrument import *

instruments = ("Astronomica", "Borealis", "Celestial", "Deuteronic", "Eclipse",
               "Floral", "Galactia", "Heliosphere", "Interstella", "Jupiter", "Koronis", "Lunatic")
counterparties = ("Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia")
NUMBER_OF_RANDOM_DEALS = 2000
TIME_PERIOD_MILLIS = 3600000
EPOCH = datetime.now() - timedelta(days=1)


class RandomDealData:
    def __init__(self):
        self.dealId = 21000
        self.instrumentList = []
        self.createInstrumentList()

    def createInstrumentList(self):
        f = open('initialRandomValues.txt', 'r')
        instrumentId = 1000
        for instrumentName in instruments:
            hashedValue = int(f.readline())
            isNegative = hashedValue < 0
            basePrice = (abs(hashedValue) % 10000) + 90.0
            drift = ((abs(hashedValue) % 5) * basePrice) / 1000.0
            drift = 0 - drift if isNegative else drift
            variance = (abs(hashedValue) % 1000) / 100.0
            variance = 0 - variance if isNegative else variance
            instrument = Instrument(instrumentId, instrumentName, basePrice, drift, variance)
            self.instrumentList.append(instrument)
            instrumentId += 1

    def createRandomData(self):
        time.sleep(random.uniform(1, 30) / 100)
        instrument = self.instrumentList[numpy.random.randint(0, len(self.instrumentList))]
        cpty = counterparties[numpy.random.randint(0, len(counterparties))]
        type = 'B' if numpy.random.choice([True, False]) else 'S'
        quantity = int(numpy.power(1001, numpy.random.random()))
        dealTime = datetime.now() - timedelta(days=1)
        self.dealId += 1
        deal = {
            'instrumentName': instrument.name,
            'cpty': cpty,
            'price': instrument.calculateNextPrice(type),
            'type': type,
            'quantity': quantity,
            'time': dealTime.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        }
        return self.dealId, deal

    def deal_generator(self):
        while True:
            nextId, next = self.createRandomData()
            yield nextId, next
