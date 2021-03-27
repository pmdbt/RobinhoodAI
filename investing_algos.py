import logging


class Buy_Dips(object):
    """
    Class for buying more stocks at dips. It's a buy only algo to build
    positions for ultra long-term durations. This strategy only calculates
    buys and no sales.
    """
    

    def __init__(self, ticker_data: dict):
        ticker_data = ticker_data


    def price_direction(self, new: float, old: float) -> str:
        """
        Method to check if the direction of a stock's movement is up or down given
        two price points that are consecutive in a specific timeframe. new is
        most recent price, t, and old is t-1, but 1 can be weekly, daily, or some
        other arbitrary time period.
        """
        if isinstance(new, float) and isinstance(old, float):
            if new > old:
                return 'up'
            elif new < old:
                return 'down'
            else:
                return 'flat'
        else:
            raise TypeError(f"""The new and old paramters have to be type float\n
                            They are currently:\n
                            new: {type(new)}\n
                            old: {type(old)}\n""")
