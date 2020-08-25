import logging
import os
import configparser
import robin_stocks as api
import configuration as config


# logging config
logging.basicConfig(format='%(levelname)s: authentication.py %(message)s',
        level=config.LOGGING_LEVEL)


class Authentication(object):
    """
    Class to automate logging into robinhood using the personal_credentials.py
    file in the .env directory the user created
    """


    def login(self):
        """
        Method to login

        :param: None
        :return: None
        """
        creds = self.fetch_credentials()
        logging.info('logging in to robinhood now...')
        login = api.login(creds.get('username'), creds.get('password'))

    
    def logout(self):
        """
        Method to logout of current robinhood session

        :param: None
        :return: None
        """
        logging.info('logging out of robinhood...')
        api.logout()


    def fetch_credentials(self):
        """
        Method to fetch credentails from .env/personal_credentials

        :param: None
        :return: creds (dict)
        """
        logging.info('fetching user credentials locally...')
        config = configparser.RawConfigParser()
        main_path = os.getcwd()
        path = f"{main_path}/.env/personal_credentials"
        logging.info(f"fetching from path: {path}")
        config.read(path)
        username = config.get('default', 'username')
        password = config.get('default', 'password')
        creds = {
                'username': username,
                'password': password 
                }
        return creds
