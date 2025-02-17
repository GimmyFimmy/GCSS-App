# import libraries
import time

import cv2

from src.utils.calculate import delay

class VideoCapture:
    def __init__(self):
        # empty variable
        self.capture = None
        self.running = False

    def start(self, image_changed, delay_value=1):
        # check if 'int' type received
        assert(type(delay_value) == int)

        # check if 'function' type received
        assert(callable(image_changed))

        # create 'video capture'
        self.capture = cv2.VideoCapture(0)

        # set 'running: bool' to true
        self.running = True

        # go through frames while 'capture' is opened
        while self.capture.isOpened():
            # read captured frames to get 'success: bool' and 'frame: ndarray'
            success, frame = self.capture.read()

            # check if 'frame: ndarray' received
            if not success:
                continue

            # call 'image_changed: function'
            image_changed(cv2.flip(frame, 1))

            # 'delay: int'
            time.sleep(delay(delay_value))

        # set 'running: bool' to false
        self.running = False

    def is_running(self):
        # return 'true' if 'capture' is opened, otherwise 'false'
        return self.running is True

    def stop(self):
        # release 'capture'
        self.capture.release()