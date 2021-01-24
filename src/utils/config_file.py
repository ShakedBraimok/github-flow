import yaml
import os
from src.utils.git import get_repo_abspath

CONFIG_FILE_NAME = "github-flow.yaml"

def read_config():
    config_file = get_config_file()
    with open(config_file, 'r') as stream:
        try:
            config = (yaml.safe_load(stream))
            return config
        except yaml.YAMLError as exc:
            return exc


def get_config_value(topic,key):
    config_file = get_config_file()
    with open(config_file, 'r') as stream:
        try:
            config = (yaml.safe_load(stream))
            return config[topic][key]
        except KeyError as exc:
                return ""



def get_config_file():
    abspath = get_repo_abspath()
    config_file = abspath + "/" + CONFIG_FILE_NAME
    return config_file

