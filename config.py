import os
import configparser
def get_number_of_papers(section: str, param_name: str):
    config_file_path = "configurations.ini"
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file_path)
    return config_parser[section][param_name]