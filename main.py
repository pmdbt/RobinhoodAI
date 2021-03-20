import logging
import authentication as auth
from data_pipeline import Robin_Pipeline
import configuration as config
import pprint

# logging config
logging.basicConfig(format='%(levelname)s: main.py %(message)s',
        level=config.LOGGING_LEVEL)


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

