import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random

stage = 'Callbacks'

logging.basicConfig(
    filename=os.path.join('logs', 'logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    filemode='a'
)

def main(path):
    config = read_yaml(path)
    pass

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', '-c', default='configs/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info('\n--------------\n')
        logging.info(f'{stage} stage started')
        main(parsed_args.config)
        logging.info(f'{stage} stage completed')
    except Exception as e:
        logging.exception(e)
        raise e