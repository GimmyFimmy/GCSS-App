# import libraries
import cv2, os.path, numpy

# paths
path_to_datasets = os.path.abspath('datasets')

def save(image: numpy.ndarray, gesture_name: str, index: int):
    # check if 'int' type received
    assert(type(index) == int)

    # check if 'str' type received
    assert(type(gesture_name) == str)

    # try to save 'image: ndarray'
    try:
        # save 'image: ndarray' as '.jpg' file
        return cv2.imwrite(
            filename=path_to_datasets + f'/{gesture_name}/{str(index)}.jpg',
            img=image
        )
    except Exception as reason:
        # raise warning
        print('failed to save %s image. reason: %s' % (gesture_name, reason))