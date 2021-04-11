import logging
import pandas as pd


class Buy_Dips(object):
    """
    Class for buying more stocks at dips. It's a buy only algo to build
    positions for ultra long-term durations. This strategy only calculates
    buys and no sales.
    """
    

    def __init__(self, ticker_data: dict):
        ticker_data = ticker_data


    def __price_direction(self, ticker_price_df: object, period: int) -> object:
        """
        Using pandas diff to find the difference between each iterative row
        given a value for the time-period.
        """
        diff_pd = ticker_price_df.diff(periods=period, axis=0)
        # diff always produces a nan row for the first row, so remove first
        diff_pd = diff_pd.drop(index=diff_pd.index, axis=0, inplace=False)
        return diff_pd


