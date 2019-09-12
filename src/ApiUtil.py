import logging

import requests
import yaml

from src.data_model import Config as Config
from src.data_model.Config import Config


class ApiUtil():

    @staticmethod
    def read_from_file(filename: str) -> dict:
        with open(filename, 'r') as ymlfile:
            data = yaml.load(ymlfile, Loader=yaml.Loader)
        return data


    @staticmethod
    def read_from_str(str: str) -> dict:
        return yaml.load(str)

    @staticmethod
    def read_config() -> Config:
        cfg = ApiUtil.read_from_file('config.yml')

        logging.debug("Configuration read")
        return Config.from_dict(cfg)

    @staticmethod
    def test_token(host, endpoint, token) -> bool:
        headers = {'X-Lola-Homework-Access-Token': token}
        result = requests.get(host + endpoint, headers=headers).json()
        try:
            result['email']
            return True
        except KeyError:
            return False