import logging
import pandas as pd


class Buy_Dips(object):
    """
    Class for buying more stocks at dips. It's a buy only algo to build
    positions for ultra long-term durations. This strategy only calculates
    buys and no sales.
    """
    

    def __init__(self, ticker_data: dict, period: int):
        self.ticker_data = ticker_data
        self.directional_data = {}
        self.diff_period = period


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
            directional_data[k] = __price_direction(
                ticker_price_df=v,
                period=self.diff_period
            )
        return directional_data
