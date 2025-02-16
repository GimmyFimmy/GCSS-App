"""
    NAME: gesture_recognizer.py

    DESC: solution for processing given image and calling results

    PRIVATE METHODS:
        __init__ --> initializes util
        __result_callback --> calls when process results received

    PUBLIC METHODS:
        process --> callbacks gesture name, image, frame timestamp ms
"""

# import libraries
import mediapipe, numpy

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import RunningMode

from src.constants import (
    Path,
    ASSET_PATH,
    DEFAULT_GESTURE
)

class GestureRecognizer:
    def __result_callback(self, *args):
        # check if 'listener: function' exists
        if self.listener:
            # reset 'gesture: str'
            gesture = DEFAULT_GESTURE

            # get 'results'
            results = args[0]

            # check if 'gestures' received
            if results.gestures:
                # set new 'gesture: str'
                gesture = results.gestures[0][0].category_name.replace('\r', '')

            # call 'listener: function'
            self.listener(gesture)

    def __init__(self, listener):
        # check if 'gesture_recognizer.task' exists
        if not Path.exists(ASSET_PATH):
            return

        assert(callable(listener))

        model_file = open(ASSET_PATH, "rb")
        model_data = model_file.read()
        model_file.close()

        # create gesture recognizer 'base options'
        self.base_options = python.BaseOptions(
            model_asset_buffer=model_data
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

        # create variables
        self.listener = listener

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