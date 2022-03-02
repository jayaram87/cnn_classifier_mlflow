import argparse
import os
import logging
from src.utils.common import read_yaml, create_directories
from src.utils.model import log_model_summary
import random
import tensorflow as tf

stage = 'BASE MODEL'

logging.basicConfig(
    filename=os.path.join('logs', 'logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    filemode='a'
)

def main(path):
    config = read_yaml(path)
    params = config['params']

    logging.info('CNN layers defined')
    layers = [
        tf.keras.layers.Input(shape=tuple(params['img_shape'])),
        tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=(2,2)),
        tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=(2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=8, activation='relu'),
        tf.keras.layers.Dense(units=2, activation='sigmoid')
    ]

    base_model = tf.keras.Sequential(layers)

    logging.info(f'base model summary {log_model_summary(base_model)}')

    base_model.compile(
        optimizer=tf.keras.optimizers.Adam(params['lr']),
        loss=params['loss'],
        metrics=params['metrics']
    )

    model_dir = os.path.join(config['data']['local_dir'], config['data']['model_dir'])
    create_directories([model_dir])

    model_path = os.join.path(model_dir, config['data']['init_model_file'])
    base_model.save(model_path)
    logging.info(f'base model has been saved {model_path}')

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', '-c', default='configs/config.yaml')
    parsed_args = args.parse_args()

    try:
        logging.info('\n----------------\n')
        logging.info(f'{stage} stage started')
        main(parsed_args.config)
        logging.info(f'{stage} stage completed')
    except Exception as e:
        logging.exception(e)
        raise e