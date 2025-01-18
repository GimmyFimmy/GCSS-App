"""
    **Description**:
        util for processing given image and returning result

    ----

    **Private Methods**:
        *__init__* --> initializes util

    ----

    **Public Methods**:
        *process* --> returns hand(s) landmarks
"""

# import libraries
import cv2, numpy

from mediapipe.python.solutions import hands

class HandDetector:
    def __init__(self, max_hands=2):
        # create hand detector with parameters
        self.Hands = hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
        )

    def process(self, image):
        # check if 'ndarray' type received
        assert (type(image) == numpy.ndarray)

        # convert 'image: ndarray' from 'BGR' to 'RGB'
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # process 'image: ndarray' and return result
        return self.Hands.process(image)