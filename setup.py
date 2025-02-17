import os

from io import BytesIO
from urllib import request
from zipfile import ZipFile

from src.constants import (
    Path,

    DATASETS_PATH,
    DEVICES_PATH,
    ASSET_PATH,
    MODEL_PATH,

    SAMPLES_LINK,
    MODEL_LINK,
)

def download_model():
    request.urlretrieve(MODEL_LINK, ASSET_PATH)

def download_samples():
    gesture_recognizer_path = 'src/libs/gesture_recognizer'

    samples = request.urlopen(SAMPLES_LINK)
    archive = ZipFile(BytesIO(samples.read()))

    archive.extractall(gesture_recognizer_path)

    os.rename(os.path.join(gesture_recognizer_path, 'rps_data_sample'), DATASETS_PATH)

if __name__ == '__main__':
    Path.create_directory(DEVICES_PATH)
    Path.create_directory(MODEL_PATH)

    download_model()
    download_samples()