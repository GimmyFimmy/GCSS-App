"""
    **Description**:
        util for processing given image and calling results

    ----

    **Private Methods**:
        *__init__* --> initializes util

    ----

    **Public Methods**:
        *process* --> callbacks gesture name, image, frame timestamp ms
"""

# import libraries
import os.path, mediapipe, numpy

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import RunningMode
from setuptools.command.alias import alias

# paths
path_to_models = os.path.abspath('models')
path_to_model_asset = os.path.join(path_to_models, 'gesture_recognizer.task')

class GestureRecognizer:
    def __init__(self, result_callback):
        # check if 'function' type received
        assert(callable(result_callback) == True)

        # create gesture recognizer 'base options'
        self.base_options = python.BaseOptions(
            model_asset_path=path_to_model_asset
        )

        # create gesture recognizer 'options'
        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=RunningMode.LIVE_STREAM,
            result_callback=result_callback
        )

        # create gesture recognizer with options
        self.recognizer = vision.GestureRecognizer.create_from_options(
            options=self.options
        )

    def process(self, image: numpy.ndarray, frame_timestamp_ms: int):
        # check if 'int' type received
        assert (type(frame_timestamp_ms) == int)

        # convert 'image: ndarray' in 'mp_image'
        mp_image = mediapipe.Image(
            image_format=mediapipe.ImageFormat.SRGB,
            data=image
        )

        # process 'mp_image' to get recognition results
        self.recognizer.recognize_async(
            image=mp_image,
            timestamp_ms=frame_timestamp_ms
        )