import pandas as pd
import numpy as np
import robin_stocks as api
import logging
import configuration as config


"""
Classes for all the data pipelines include ticker data from Robinhood, but
also external data from 3rd party sources.
"""

# logging config
logging.basicConfig(format='%(levelname)s: data_pipeline.py %(message)s',
        level=config.LOGGING_LEVEL)

class Robin_Pipeline(object):
    """
    Class for interacting with the robinhood api to pull in ticker and other
    asset level information including historical data
    """


    def __init__(self, ticker_list: list, needs_fractional: bool) -> None:
        self.tickers = ticker_list
        self.needs_fractional = needs_fractional


    def set_tickers(self, tickers: list) -> None:
        """
        method to mutate the object variable-tickers
        """
        self.tickers = tickers


    @static_method
    def check_ticker(tickers: list) -> dict or None:
        """
        method used to check if a list of tickers exists on robinhood and can actually
        be traded or not.
        """
        results = api.stocks.get_instruments_by_symbols(inputSymbols=tickers)
        if results:
            tradability = {}
            for ticker_result in results:
                tradability[ticker_result.get('symbol')] = {
                    'tradable': ticker_result.get('tradable'),
                    'fractional_tradability': ticker_result.get('fractional_tradability')
                }
            return tradability
        else:
            logging.info(f"""
                         Custom Logging Message:\n
                         Robinhood API not returning results for ticker query at
                         method check_ticker in data_pipeline.py.
                         """)


    def filter_tickers(self) -> list:
        """
        method to take the initialized list of tickers and checks each individual tickers to make
        sure that the inputed tickers can be actively traded and validates if fractional trading
        is enabled based on the strategy requirement. If the tickers cannot be traded, then the
        list is edited to remove those tickers that cannot be traded. If all tickers cannot be
        traded, then the list becomes empty and no trades will be executed.
        """
        tradability = check_ticker(self.tickers)
        if self.needs_fractional == False:
            tradable_tickers = [for ticker in tradability if tradable_tickers.get(ticker).get('tradable') == True]
        else:
            tradable_tickers = [for ticker in tradability
                                 if tradable_tickers.get(ticker).get('tradable') == True
                                 and tradable_tickers.get(ticker).get('fractional_tradability') == True]
        return tradable_tickers


    def select_tickers(self) -> None:
        """
        Checks and sets the tickers according to if they are tradable and whether it fits with the
        specified strategy when it comes to fractional shares.
        """
        logging.info("Checking if desired tickers are tradable...")
        new_tickers = filter_tickers()
        logging.info("Setting new tickers...")
        self.set_tickers(tickers=new_tickers)

