import json
import logging

PRICE=0
QUANTITY=0
class SimpleStrategy:

    def __init__(self,gateway,threshold):
        self.orders=[]
        self.gateway=None
        self._current_data=None
        self.threshold=threshold
        self.orders=[]

    def _parseInput(self,body):
        self._current_data=json.loads(body)


    def _huobi_time(self):
        return self._current_data['huobi']['ts']
    def _huobi_ask_bid(self):
        return self._current_data['huobi']
    def _okx_ask_bid(self):
        return self._current_data['okx']
    def _okx_time(self):
        return self._current_data['okx']['ts']

    def strategy(self,body):
        self._parseInput(body)
        huobi_ticks=self._huobi_ask_bid()
        okx_ticks=self._okx_ask_bid()
        try:
            print("-------------------------------------------------------------------------------------------")
            if  huobi_ticks['bids'][0][PRICE]-okx_ticks['asks'][0][PRICE]>self.threshold:
                logging.info("Huobi sell order at " +str(huobi_ticks['bids'][0][PRICE]))
                logging.info("okx buy order at "+str(okx_ticks['asks'][0][PRICE]))

            elif okx_ticks['bids'][0][PRICE]-huobi_ticks['asks'][0][PRICE]>self.threshold:
                logging.info("Huobi buy order at "+str(huobi_ticks['asks'][0][PRICE]))
                logging.info("okx sell order at "+str(okx_ticks['bids'][0][PRICE]))
            else:
                print("No arbitrage opportunity")

        except IndexError:
            logging.info("No asks or bids")

