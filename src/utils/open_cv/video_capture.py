# import libraries
import cv2

class VideoCapture:
    def __init__(self, ):
        # create video capture
        self.capture = cv2.VideoCapture(0)

    def start(self, image_changed):
        # check if 'function' type received
        assert (callable(image_changed) == True)

        # check if 'capture' is opened
        assert(self.running() == False)

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
            cv2.waitKey(1)

    def running(self):
        # return 'true' if 'capture' is opened, otherwise 'false'
        return self.capture.isOpened()

    def stop(self):
        # check if 'capture' is not opened
        assert(self.running() == True)

        # release 'capture'
        self.capture.release()