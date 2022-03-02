import os
import yaml
import logging
import time
import pandas as pd
import json
from zipfile import ZipFile

def read_yaml(path: str) -> dict:
    with open(path) as file:
        content = yaml.safe_load(file)
    logging.info(f'yaml file: {path} has been loaded successfully')
    return content

def create_directories(paths: list) -> None:
    for path in paths:
        os.makedirs(path, exist_ok=True)
        logging.info(f'{path} directory created')

def save_json(path: str, data: dict) -> None:
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    logging.info(f'json file {file} saved')

def unzip_file(source: str, dest: str) -> None:
    logging.info(f'extraction started...')
    with ZipFile(source, 'r') as zip_f:
        zip_f.extractall(dest)
    logging.info(f'extracted {source} to {dest}')