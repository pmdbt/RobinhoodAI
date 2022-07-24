from analysis.py import Directional_Analysis
import pandas as pd
import pytest


def test_price_direction():
    """
    Find out if pandas diff method is returning the expected results with
    different periods
    """
    dummy_data = {
        ''
    }
    algo = Directional_Analysis(ticker_data=, period=1)
    ###
    algo = Directional_Analysis(ticker_data=None, period=1)
    """Scenario 1"""
    test_old, test_new = 124.4, 100.25323
    test_result = algo.__price_direction(new=test_new, old=test_old)
    assert test_result == 'down', f"""
    The returned result should be 'down', but the result was {test_result}
    """
    """Scenario 2"""
    test_old, test_new = 99.99, 2000.02
    test_result = algo.price_direction(new=test_new, old=test_old)
    assert test_result == 'up', f"""
    The returned result should be 'up', but the result was {test_result}
    """
    """Scenario 3"""
    test_old, test_new = 10.202, 10.202
    test_result = algo.price_direction(new=test_new, old=test_old)
    assert test_result == 'flat', f"""
    The returned result should be 'flat', but the result was {test_result}
    """
    """Scenario 4"""
    test_old, test_new = 2, 'abcde'
    with pytest.raises(TypeError):
        test_result = algo.price_direction(new=test_new, old=test_old)

