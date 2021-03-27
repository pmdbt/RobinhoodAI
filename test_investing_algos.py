from investing_algos import Buy_Dips
import pytest


def test_price_direction():
    """
    unit test for the price_direction() method. There are 3 scenarios in which
    the method should return the strings 'up', 'down', or 'flat'. The parameters
    have to be floating digits or else an error will be raised. This test also
    tests for this 4th scenario.
    """
    # create object
    algo = Buy_Dips(ticker_data=None)
    """Scenario 1"""
    test_old, test_new = 124.4, 100.25323
    test_result = algo.price_direction(new=test_new, old=test_old)
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

