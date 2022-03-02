import mlflow
import argparse
import os
import logging
from src.utils.common import read_yaml, create_directories

stage = 'main'

create_directories(['logs'])

logging.basicConfig(
    filename=os.path.join('logs', 'logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    filemode='a'
)

def main():
    with mlflow.start_run() as run:
        mlflow.run('.', 'get_data', use_conda=False)
        mlflow.run('.', 'base_model_creation', use_conda=False)
        #mlflow.run('.', 'training', use_conda=False)

if __name__ == '__main__':
    try:
        logging.info(f'{stage} stage started\n')
        main()
        logging.info(f'{stage} stage completed\n')
    except Exception as e:
        logging.exception(e)
        raise e
