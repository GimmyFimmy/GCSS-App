import os.path
import cv2
import mediapipe

from Shared.Mediapipe.ModelTrainer import path_to_models
from Shared.OpenCV.VideoCapture import VideoCapture
from Shared.Mediapipe.HandDetector import HandDetector

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import RunningMode
from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizerResult

path_to_model = os.path.join(path_to_models, 'gesture_recognizer.task')

class GestureRecognizer:
    def __init__(self, display_video=False):
        self.base_options = python.BaseOptions(
            model_asset_path=path_to_model
        )

        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=RunningMode.LIVE_STREAM,
            result_callback=self.__on_gesture_recognized
        )

        self.recognizer = vision.GestureRecognizer.create_from_options(
            self.options
        )

        self.VideoCapture = VideoCapture(
            display_video=display_video,
            display_name='GestureRecognizer'
        )

        self.HandDetector = HandDetector(
            max_hands=2,
            draw_landmarks=True,
        )

        self.current_gesture = 'None'

    def __on_gesture_recognized(self, result: GestureRecognizerResult, output_image: mediapipe.Image, timestamp: int):
        if not result.gestures:
            print("no gesture received!")
            return

        self.current_gesture = str(result.gestures[0][0].category_name)
        print(self.current_gesture)

    def __on_frame_changed(self, image):
        result = self.HandDetector.process(image)

        if result.multi_hand_landmarks:
            image = mediapipe.Image(
                image_format=mediapipe.ImageFormat.SRGB,
                data=image
            )

            frame_timestamp = self.VideoCapture.capture.get(cv2.CAP_PROP_POS_MSEC)

            self.recognizer.recognize_async(
                image=image,
                timestamp_ms=int(frame_timestamp)
            )

    def start_recognition(self):
        self.VideoCapture.start_capture(self.__on_frame_changed)

    def stop_recognition(self):
        self.VideoCapture.stop_capture()

    def get_current_gesture(self):
        if self.VideoCapture.running == True:
            return self.current_gesture