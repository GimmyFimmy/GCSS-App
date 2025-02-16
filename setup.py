import urllib.request

from src.constants import (
    Path,

    DATASETS_PATH,
    DEVICES_PATH,
    ASSET_PATH,
    MODEL_PATH,

    SAMPLES_LINK,
    MODEL_LINK
)

def download_model():
    urllib.request.urlretrieve(MODEL_LINK, MODEL_PATH)

def download_samples():
    IMAGE_FILENAMES = ['thumbs_down.jpg', 'victory.jpg', 'thumbs_up.jpg', 'pointing_up.jpg']

    for name in IMAGE_FILENAMES:
        directory = f'{DATASETS_PATH}/{name}'
        url = f'{SAMPLES_LINK}{name}'

        urllib.request.urlretrieve(url, directory)

if __name__ == '__main__':
    Path.create_directory(DATASETS_PATH)
    Path.create_directory(f'{DATASETS_PATH}/None')

    Path.create_directory(DEVICES_PATH)
    Path.create_directory(MODEL_PATH)

    #download_model()
    download_samples()