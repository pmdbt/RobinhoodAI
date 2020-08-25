# Robinhood Trading AI

By: Jerry Chu (pmdbt)[https://github.com/pmdbt]
Maintained By: Jerry Chu (pmdbt)[https://github.com/pmdbt]

### Description:

This is a personal project of mine to build a suite of A.I. agents to trade different financial instruments through Robinhood's API for my personal account. The goal is to the agents using daily data going back as far as robinhood's historical data allows. I'll use a similar strategy to pair-wise trading that's been common with quants in the past. For any target instrument, the goal is to ingest data of it along with a few closely related instruments. One example is trading shares of AMD, but using historical data of AMD, Intel, and NVidia at the same time. The agent should be able to use time-series data of multiple assets and learn patterns of relationships between the instruments, then make predictions of future prices 1 day into the future. Each daily open, the agent would place 1 order based on predictions, then close the position by market close regarless of position outcomes.

### File Structure:
WIP

### Unit Tests:
WIP

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


