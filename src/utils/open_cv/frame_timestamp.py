#import libraries
import cv2

def calculate(capture):
    # return 'frame timestamp ms: int'
    return int(capture.get(cv2.CAP_PROP_POS_MSEC))