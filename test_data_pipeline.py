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
        "tickers":  ['ABC', 'EFG'],
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
    Object variables: {instance_vars}\n
    """


def test_set_tickers():
    """
    Method to test if the set_ticker method is working as intended.
    """
    original_tickers = ['test1', 'test2']
    new_tickers = ['new', 'new2']
    needs_fractional = True
    test_obj = Robin_Pipeline(
        tickers=original_tickers,
        needs_fractional=needs_fractional)
    test_obj.set_tickers(tickers=new_tickers)
    assert test_obj.tickers == list(map(str.upper, new_tickers)), f"""
    The new tickers set do not equal the new values passed into the setter's
    parameters.\n
    original tickers: {original_tickers}\n
    new_tickers: {new_tickers}\n
    object tickers after running setter method: {test_obj.tickers}\n
    """

def test_set_tickers_raise_correct_errors():
    test_dict = {
        "tickers": ['test1', 'test2'], 
        "needs_fractional":  False
    }
    test_obj = Robin_Pipeline(
        tickers=test_dict['tickers'],
        needs_fractional=test_dict['needs_fractional'])
    with pytest.raises(TypeError):
        test_obj.set_tickers(tickers="aapl")
    with pytest.raises(ValueError):
        test_obj.set_tickers(tickers=[])
    with pytest.raises(ValueError):
        test_obj.set_tickers(tickers=None)


def test_set_needs_fractional():
    """
    func to test if set_needs_fractional is working as intended
    """
    test_dict = {
        "tickers": ['test1', 'test2'], 
        "needs_fractional":  False
    }
    test_obj = Robin_Pipeline(
        tickers=test_dict['tickers'],
        needs_fractional=test_dict['needs_fractional'])
    new_command = True
    test_obj.set_needs_fractional(new_command)
    assert test_obj.needs_fractional == new_command


def test_set_needs_fractional_raise_correct_errors():
    """
    Func to test if the correct errors are being raised given specific
    paramters
    """
    test_dict = {
        "tickers": ['test1', 'test2'], 
        "needs_fractional":  False
    }
    test_obj = Robin_Pipeline(
        tickers=test_dict['tickers'],
        needs_fractional=test_dict['needs_fractional'])
    with pytest.raises(TypeError):
        test_obj.set_needs_fractional(None)
    with pytest.raises(TypeError):
        test_obj.set_needs_fractional('')


def test_check_ticker():
    """
    Method to test the check_ticker() method returns a dict or not
    """
    test_tickers = ['aapl', 'gme', 'tsla']
    needs_fractional = False
    test_obj = Robin_Pipeline(
        tickers=test_tickers,
        needs_fractional=needs_fractional)
    results = test_obj.check_ticker(tickers=test_obj.tickers)
    for key in results:
        assert key in [ticker.upper() for ticker in test_tickers], f"""
        A key in the results dictionary is not a member of the test_tickers
        list.\n
        test_tickers list: {test_tickers}\n
        key: {key}\n
        """
