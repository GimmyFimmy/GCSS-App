# import libraries
import cv2

from src.constants import MAX_ACCURACY_PERCENTAGE

def frame_timestamp(video_capture: cv2.VideoCapture):
    # return 'frame timestamp ms: int'
    return int(video_capture.get(cv2.CAP_PROP_POS_MSEC))

def accuracy(value: int):
    # return 'accuracy: int'
    return round(value * MAX_ACCURACY_PERCENTAGE)