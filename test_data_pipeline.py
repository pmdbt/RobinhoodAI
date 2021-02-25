import pytest
from data_pipeline import Robin_Pipeline


"""
Tests for the Robin_Pipeline class
"""


def test_init():
    """
    Method to test if the init func is working as intended in the class.
    """
    test_dict = {
        "tickers":  ['test1', 'test2'],
        "needs_fractional":  False
    }
    test_obj = Robin_Pipeline(
        tickers=test_dict['tickers'],
        needs_fractional=test_dict['needs_fractional'])
    # find all instance variables
    instance_vars = vars(test_obj)
    # check if the variables are the same as in the test dict
    assert test_dict == instance_vars, f"""
    Object has different variables than the original initialized ones.\n
    Original init variables: {test_dict}\n
    Object variables: {instance_vars}
    """


def test_set_tickers():
    """
    Method to test if the set_ticker method is working as intended.
    """
    original_tickers = ['test1', 'test2']
    new_tickers = ['new']
    needs_fractional = True
    test_obj = Robin_Pipeline(
        tickers=original_tickers,
        needs_fractional=needs_fractional)
    test_obj.set_tickers(tickers=new_tickers)
    assert test_obj.tickers == new_tickers, f"""
    The new tickers set do not equal the new values passed into the setter's
    parameters.\n
    original tickers: {original_tickers}\n
    new_tickers: {new_tickers}\n
    object tickers after running setter method: {test_obj.ticker_list}\n
    """
