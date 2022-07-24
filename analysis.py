import logging
from data_pipeline import Robin_Pipeline
import numpy as np
import configuration as config


"""
Classes for performing analysis on pipeline data
"""

# logging config
logging.basicConfig(format='%(levelname)s: analysis.py %(message)s',
        level=config.LOGGING_LEVEL)

# basic analysis class for inhertiance
class Transform(object):
    """
    Class with methods to perform basic data manipulation such as spliting
    dataframes or extracting columns of data etc
    """
    def __init__(self, ticker_data: dict):
        if ticker_data:
            self.ticker_data = ticker_data
        else:
            logging.warning(f"""
                            The ticker_data dictionary is empty during
                            initialization. Exiting for safety.
                            """)
            exit()


    def __select_ticker_analysis(self, ticker_symbol: str) -> pd.DataFrame:
        """
        Method to extract the dataframe of data of a specific ticker from
        a dictionary of tickers and dataframes.
        """
        return self.ticker_data[ticker_symbol]


    def __extract_column(
        self,
        df: pd.DataFrame,
        column_name: str,
        dtype: str) -> np.ndarray:
        """
        Method to extract or choose series from a dataframe and return it as
        a numpy array with diresired data type
        """
        return df[column_name].to_numpy(dtype=dtype)

    
class Directional_Analysis(Transform):
    """
    Class for analyzing the direction of price movements of asset prices
    between each row in a structured data set.
    """


    def __init__(self, ticker_data: dict, period: int):
        self.ticker_data = ticker_data
        self.directional_data = {}
        self.diff_period = period
        self.summary_data = None


    def __price_direction(self, ticker_price_df: object, period: int) -> object:
        """
        Using pandas diff to find the difference between each iterative row
        given a value for the time-period.
        """
        diff_pd = ticker_price_df.diff(periods=period, axis=0)
        # diff always produces a nan row for the first row, so remove first
        diff_pd = diff_pd.drop(index=diff_pd.index, axis=0, inplace=False)
        return diff_pd


    def find_directional_movement(self) -> dict:
        """
        Use self.__price_direction() to find price directions for every ticker
        selected iteratively and then return all price directions for each
        ticker in a dictionary
        """
        directional_data = {}
        for k, v self.ticker_data.items():
            price_direction = __price_direction(
                ticker_price_df=v,
                period=self.diff_period
            )
            if price_direction.isnull().values.any():
                logging.warning(f"""There are NaN values in the directional
                                data for {k}""")
           directional_data[k] = v 
        return directional_data


    def __set_directional_data(self):
        """
        private method to set the self.directional data variable to a
        dictionary with each ticker as the key and an object of price data
        where one column is the directional price movement between each row's
        price.
        """
        self.directional_data = self.find_directional_movement()
