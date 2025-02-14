"""
    NAME: gesture_recognizer.py

    DESC: high-level library for gesture recognition,
    hand detection and model training. It was specifically
    created for simple use and customization

    NOTE: gesture_recognizer.py must be initialized before
    any other solution, otherwise 'RunTime' error will occur

    TODO: optimize datasets
"""

# import libraries
from src.libs.gesture_recognizer.solutions.gesture_recognizer import GestureRecognizer
from src.libs.gesture_recognizer.solutions.model_trainer import ModelTrainer
from src.libs.gesture_recognizer.solutions.hand_detector import HandDetector