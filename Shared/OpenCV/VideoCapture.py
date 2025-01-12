import cv2

class VideoCapture():
    def __init__(self, display_video=False, display_name="VideoCapture"):
        self.running = False

        self.display_name = display_name
        self.display_video = display_video

    def start_capture(self, frame_changed: ()):
        if self.running == True:
            print("attempted to call 'start_capture' function twice!")
            return

        self.running = True

        self.capture = cv2.VideoCapture(0)

        while self.capture.isOpened():
            success, frame = self.capture.read()

            if not success:
                print("something went wrong!")
                continue

            frame = cv2.flip(frame, 1)

            if self.display_video == True:
                cv2.imshow(self.display_name, frame)

            frame_changed(frame)

            cv2.waitKey(1)

    def stop_capture(self):
        if self.running == False:
            print("attempted to call 'stop_capture' function twice!")
            return

        self.running = False

        self.capture.release()
        cv2.destroyAllWindows()