import logging
import authentication as auth
from data_pipeline import Robin_Pipeline
import configuration as config
import pprint

# logging config
logging.basicConfig(format='%(levelname)s: main.py %(message)s',
        level=config.LOGGING_LEVEL)


def price_direction(new: float, old: float) -> str:
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


if __name__ == "__main__":
    # create auth obj
    auth = auth.Authentication()
    # login
    auth.login()
    # create pipeline obj
    pipeline = Robin_Pipeline(tickers=config.BUY_ONLY_TICKERS, needs_fractional=True)
    # filter tickers
    pipeline.finalize_tickers()
    logging.info(f"""Final list of tickers based on trading requirements are:\n{pipeline.tickers}""")
    # query historical data
    pipeline.to_dataframes(interval='day', span='month')
    pprint.pprint(pipeline.historical_data)
    # logout
    auth.logout()

