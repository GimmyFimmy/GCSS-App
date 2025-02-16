"""
    NAME: hand_detector.py

    DESC: solution for processing given image and returning result

    PRIVATE METHODS:
        __init__ --> initializes util

    PUBLIC METHODS:
        process --> returns hand(s) landmarks
"""

# import libraries
import cv2, numpy

from mediapipe.python.solutions import hands

from src.constants import (
    MIN_TRACKING_CONFIDENCE,
    MIN_DETECTION_CONFIDENCE,
    MAX_HANDS
)

class HandDetector:
    def __init__(self):
        # create hand detector with parameters
        self.Hands = hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE
        )

    def process(self, image: numpy.ndarray):
        # process 'image: ndarray' and return result
        return self.Hands.process(image)