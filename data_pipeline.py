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
    def check_ticker(self, tickers: list) -> dict or None:
        """
        method used to check if a list of tickers exists on robinhood and can actually
        be traded or not.
        """
        results = api.stocks.get_instruments_by_symbols(inputSymbols=tickers)
        if results:
            tradability = {}
            for ticker_result in results:
                tradability[ticker_result.get('symbol')] = {
                    'tradeable': ticker_result.get('tradeable'),
                    'fractional_tradability': ticker_result.get('fractional_tradability')
                }
            return tradability
        else:
            logging.info(f"""
                         Custom Logging Message:\n
                         Robinhood API not returning results for ticker query at
                         method check_ticker in data_pipeline.py.
                         """)
