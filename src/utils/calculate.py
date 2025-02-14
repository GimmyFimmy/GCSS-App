# import libraries
import cv2, tkinter

from src.constants import MAX_ACCURACY_PERCENTAGE

def frame_timestamp(video_capture: cv2.VideoCapture):
    # return 'frame timestamp ms: int'
    return int(video_capture.get(cv2.CAP_PROP_POS_MSEC))

def accuracy(value: int):
    # return 'accuracy: int'
    return round(value * MAX_ACCURACY_PERCENTAGE)

def screen_center(window, size_x: float, size_y: float):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (size_x / 2)
    y = (screen_height / 2) - (size_y / 2)

    return int(x), int(y)