"""
    **Description**:
        util for processing given image and returning result

    ----

    **Private Methods**:
        *__init__* --> initializes util

    ----

    **Public Methods**:
        *process* --> returns hand(s) landmarks

        *draw* --> draws hand(s) landmarks
"""

# import libraries
import cv2, numpy

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

class HandDetector:
    def __init__(self, max_hands=2):
        # create hand detector with parameters
        self.Hands = hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
        )

    def process(self, image: numpy.ndarray):
        # convert 'image: ndarray' from 'BGR' to 'RGB'
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # process 'image: ndarray' and return result
        return self.Hands.process(image)

    def draw(self, image: numpy.ndarray, multi_hand_landmarks=None):
        # check if 'multi_hand_landmarks' received
        if multi_hand_landmarks:
            # go through 'multi_hand_landmarks'
            for hand_landmarks in multi_hand_landmarks:
                # draw 'connections'
                drawing_utils.draw_landmarks(
                    image=image,
                    landmark_list=hand_landmarks,
                    connections=hands.HAND_CONNECTIONS
                )