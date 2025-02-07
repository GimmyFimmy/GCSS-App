import numpy

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

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