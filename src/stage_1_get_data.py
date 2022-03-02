import argparse
from distutils.log import INFO
import os
import shutil
import logging
from src.utils.common import read_yaml, create_directories, unzip_file
from src.utils.data_mgmt import validate_image
import random
import urllib.request as req

stage = 'GET_DATA'

logging.basicConfig(
    filename=os.path.join('logs', 'logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode='a'
)

def main(path):
    config = read_yaml(path)
    url = config['data']['source_url']
    local_dir = config['data']['local_dir']
    create_directories([local_dir])

    file = config['data']['data_file']
    file_path = os.path.join(local_dir, file)
    unzip_data_dir = config['data']['unzip_data_dir']

    if not os.path.isfile(file_path):
        logging.info('file downloading')
        filename, headers = req.urlretrieve(url, file_path)
        logging.info(f'{filename} created with info {headers} \n')
        create_directories([unzip_data_dir])
        unzip_file(source=file_path, dest=unzip_data_dir)
    else:
        logging.info(f'{file} is available')
        logging.info(f'data already extracted')

    validate_image(config)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", '-c', default='configs/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info(f'--------------\n')
        logging.info(f'{stage} stage started')
        main(parsed_args.config)
        logging.info(f'{stage} stage completed')
    except Exception as e:
        logging.exception(e)
        raise e