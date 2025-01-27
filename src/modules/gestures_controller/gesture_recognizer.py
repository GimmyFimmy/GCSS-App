"""
    **Description**:
        util for processing given image and calling results

    ----

    **Private Methods**:
        *__init__* --> initializes util

        *__result_callback* --> calls when process results received

    ----

    **Public Methods**:
        *process* --> callbacks gesture name, image, frame timestamp ms

        *set_listener* --> sets new process results listener
"""

# import libraries
import os.path, mediapipe, numpy

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import RunningMode

# paths
path_to_models = os.path.abspath('models')
path_to_model_asset = os.path.join(path_to_models, 'gesture_recognizer.task')

class GestureRecognizer:
    def __result_callback(self, *args):
        # check if 'listener: function' exists
        if self.listener:
            # reset 'gesture: str'
            gesture = 'none'

            # get 'results'
            results = args[0]

            # check if 'gestures' received
            if results.gestures:
                # set new 'gesture: str'
                gesture = results.gestures[0][0].category_name

            # call 'listener: function'
            self.listener(gesture)

    def __init__(self):
        # create gesture recognizer 'base options'
        self.base_options = python.BaseOptions(
            model_asset_path=path_to_model_asset
        )

        # create gesture recognizer 'options'
        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=RunningMode.LIVE_STREAM,
            result_callback=self.__result_callback
        )

        # create gesture recognizer with options
        self.recognizer = vision.GestureRecognizer.create_from_options(
            options=self.options
        )

        # empty variables
        self.listener = None

    def set_listener(self, result_callback):
        # check if 'function' type received
        if not callable(result_callback):
            return

        # set new 'listener: function'
        self.listener = result_callback

    def process(self, image: numpy.ndarray, frame_timestamp_ms: int):
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