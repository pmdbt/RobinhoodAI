import logging
import authentication as auth
import configuration as config

# logging config
logging.basicConfig(format='%(levelname)s: main.py %(message)s',
        level=config.LOGGING_LEVEL)


if __name__ == "__main__":
    # create auth obj
    auth = auth.Authentication()
    # login
    auth.login()
    # logout
    auth.logout()
