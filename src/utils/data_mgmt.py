import shutil
import imghdr # image validation library
import os
from PIL import Image
import logging
from src.utils.common import create_directories

def validate_image(config: dict) -> None:
    parent_dir = os.path.join(
        config['data']['unzip_data_dir'],
        config['data']['parent_data_dir'])
    bad_data_dir = os.path.join(
        config['data']['unzip_data_dir'],
        config['data']['bad_data_dir'])

    create_directories([parent_dir, bad_data_dir])

    for dirs in os.listdir(parent_dir):
        full_path_data_dir = os.path.join(parent_dir, dirs)
        for imgs in os.listdir(full_path_data_dir):
            img_path = os.path.join(full_path_data_dir, imgs)
            try:
                img = Image.open(img_path)
                img.verify()
                
                # check image has 3 channels or extension is jpeg or png
                if len(img.getbands()) != 3 or imghdr.what(img_path) not in ['jpeg', 'png']:
                    bad_data_path = os.path.join(bad_data_dir, imgs)
                    shutil.move(img_path, bad_data_path)
                    logging.info(f'{img_path} file the correct format')
                    continue
            except Exception as e:
                logging.info(f'{img_path} not the right format')
                bad_data_path = os.path.join(bad_data_dir, imgs)
                shutil.move(img_path, bad_data_path)
                logging.info(f'{img_path} file moved to {bad_data_path}')
                logging.exception(e)
