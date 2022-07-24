import pandas as pd
import numpy as np
import robin_stocks as api
import logging
import configuration as config


"""
Classes for all the data pipelines include ticker data from Robinhood, but
also external data from 3rd party sources. Currently, Robinhood does not
require account authentication to ping their pipeline APIs.
"""

# logging config
logging.basicConfig(format='%(levelname)s: data_pipeline.py %(message)s',
        level=config.LOGGING_LEVEL)

class Robin_Pipeline(object):
    """
    Class for interacting with the robinhood api to pull in ticker and other
    asset level information including historical data
    """


    def __init__(self, tickers: list, needs_fractional: bool) -> None:
        self.set_tickers(tickers=tickers)
        self.set_needs_fractional(needs_fractional)
        self.historical_data = {}


    def set_tickers(self, tickers: list) -> None:
        """
        method to mutate the object variable-tickers, only accepts list dtype
        input
        """
        if tickers:
            if not isinstance(tickers, list):
                raise TypeError(f"""the input for tickers is type {type(tickers)}
                                 and not a list, which is not allowed. please
                                 use a list of tickers instead. exiting...""")
            else:
                self.tickers = [ticker.upper() for ticker in tickers]
        else:
            raise ValueError(f"""the input for tickers is {tickers} of type \
            {type(tickers)} and not a list, which is not allowed. please\
            use a list of strings for tickers. exiting...""")


    def set_needs_fractional(self, needs_fractional: bool) -> None:
        """
        method to mutate the object variable-needs_fractional. Only accepts
        bool dtype
        """
        if isinstance(needs_fractional, bool):
            self.needs_fractional = needs_fractional
        else:
            raise TypeError(f"""needs_fractional needs to be type bool in\
                            set_needs_fractional, but was type\
                            {type(needs_fractional)} instead.""")


    @staticmethod
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
                    'tradable': ticker_result.get('tradeable'),
                    'fractional_tradability': ticker_result.get('fractional_tradability')
                }
            # checks if tradable and fractional_tradability have the right values
            for key in tradability:
                for sub_key in tradability[key]:
                    value = tradability[key][sub_key]
                    if sub_key == 'tradable':
                        if not isinstance(value, bool):
                            raise TypeError(f"""The allowed values for
                            tradability is only bool True or False values. The
                            value for {sub_key} is {value} of type {type(value)}.""")
                    elif sub_key == 'fractional_tradability':
                        if not isinstance(value, str):
                            raise TypeError(f"""The allowed values for
                            fractional_tradability is only bool True or False
                            values. The value for {sub_key} is {value} of type
                            {type(value)}.""")
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
        tradability = self.check_ticker(self.tickers)
        if self.needs_fractional == False:
            tradable_tickers = [ticker for ticker in tradability if tradability.get(ticker).get('tradable') == True]
        else:
            tradable_tickers = [ticker for ticker in tradability
                                 if tradability.get(ticker).get('tradable') == True
                                 and tradability.get(ticker).get('fractional_tradability') == 'tradable']
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


    def finalize_tickers(self) -> None:
        """
        Method to set the self.tickers variable to tickers that have passed
        the filtering criteria based on whether they're tradable and if they
        are fractionally tradable.
        """
        tradable_tickers = self.filter_tickers()
        self.set_tickers(tickers=tradable_tickers)


    def query_historical_data(self, ticker: str, interval: str, span: str) -> list:
        """
        Method to query to historical data for a single stock or a list of stocks
        Returns a list of dictionaries
        """
        query_results = api.stocks.get_stock_historicals(ticker, interval=interval, span=span)
        return query_results


    def to_dataframes(self, interval: str, span: str) -> None:
        """
        Method to convert lists of dictionaries of historical ticker data into pandas dataframes
        """
        dict_storage = {}
        for ticker in self.tickers:
            query_results = self.query_historical_data(ticker, interval=interval, span=span)
            if query_results:
                dict_storage[ticker] = pd.DataFrame.from_records(query_results, index='begins_at')
            else:
                logging.warning(f"""The ticker symbole {ticker} is not returning valid data in to_dataframes()\n
                it is returning: {query_results}""")
                continue

        if dict_storage:
            self.historical_data = dict_storage
        else:
            raise TypeError(f"""dict_storage in to_dataframes() cannot be empty or None.\nIt is: {dict_storage}""")
