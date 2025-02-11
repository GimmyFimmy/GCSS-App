# import libraries
import cv2, numpy

from src.constants import DATASETS_PATH

def save(image: numpy.ndarray, name: str, index: int):
    # try to save 'image: ndarray'
    try:
        # save 'image: ndarray' as '.jpg' file
        cv2.imwrite(
            filename=DATASETS_PATH + f'/{name}/{str(index)}.jpg',
            img=image
        )
    except OSError:
        # raise error
        print(f'[ERROR]: unable to save {name} image')