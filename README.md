# Robinhood Trading AI

By: Jerry Chu (pmdbt)[https://github.com/pmdbt]\
Maintained By: Jerry Chu (pmdbt)[https://github.com/pmdbt]

### Description:

This is a personal project of mine to build a suite of A.I. agents to trade different financial instruments through Robinhood's API for my personal account. The goal is to the agents using daily data going back as far as robinhood's historical data allows. I'll use a similar strategy to pair-wise trading that's been common with quants in the past. For any target instrument, the goal is to ingest data of it along with a few closely related instruments. One example is trading shares of AMD, but using historical data of AMD, Intel, and NVidia at the same time. The agent should be able to use time-series data of multiple assets and learn patterns of relationships between the instruments, then make predictions of future prices 1 day into the future. Each daily open, the agent would place 1 order based on predictions, then close the position by market close regarless of position outcomes.


### Strategies:

This repo will contain many trading strategies, not all of which will be
ML/AI based. The following strategies are currently included:

~Non-ML based~:

- Buy-And-Hold: One of the best ways to build long term wealth is to consistently
buy equity over-time and let the long-term appreciation over many decades act
with a compounding effect to grow one's wealth. Sadly, very few people actually
have the self discipline to pull this off. As a result, an automated approach
can be very useful. This strategy will require one to consistently deposit funds
into one's robinhood account over time either through automated deposits or
manual deposites periodically. The strategy will purchase shares in the major
USA based indices and one world index consistently over time without ever selling.
The alorithm will check to see if today's opening price is lower or higher than
the previous day's opening price. If it's lower, it will purchase shares equivalent
to the nearest whole number that's 5% of an account's available cash position. The
idea is to buy shares as the markets are going down, since short term gains are
not relevant to this strategy. We want to build long term wealth over decades
by buying whenever the market dips. Using a percentage based purchase will make
sure the account never buys more than the currently available cash position and
will prevent this strategy from employing margin.

~ML based~:

WIP

### File Structure:
WIP

### Unit Tests:

This repo uses the pytest framework for testing. The test file is `test_project.py`
and one can easily run the tests with `pytest test_project.py` as long as the pytest
module is installed correctly.

### Deployment Locally:
WIP

### Deployment On The Cloud:
WIP

### Batch Learning:
WIP

### Online Learning:
WIP

### TO DOs:

1. Add configuration.py file to set ticker constants for instruments to trade as well as timeframe to trade and order size
2. - Add function to pull historical data for desired tickers from Robinhood's historical data
   - Add functions to clean and organize the historical data into a nice numpy array
   - Use the sklearn train and test split to split the data for training
3. Add deep_learning.py with the first neural network architecture


