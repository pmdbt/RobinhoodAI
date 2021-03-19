import pytest
from authentication import Authentication


@pytest.fixture(scope="module")
def auth():
    return Authentication()


def test_fetch_credentails(auth):
    """
    Func to test if the fetch_credentials() method is working as intended.
    """
    creds = auth.fetch_credentials()
    # make sure none of the variables and dictionary keys are empty
    assert creds != None, f"""Credentials cannot be empty or invalid. It's currently
    {creds}"""
    assert creds['username'] != None and creds['username'] != '', f"""username
    cannot be empty or None. It's currently {creds['username']}"""
    assert creds['password'] != None and creds['password'] != '', f"""password
    cannot be empty or None. It's currently {creds['password']}"""


"""
Can't write tests for login and log out methods because of 2FA. There is no way
to automatically get the authenticator code to input into the login stdin, so the
test will always fail. For now, we assume if you can fetch the proper credentials
the login and logout methods will work.
"""
