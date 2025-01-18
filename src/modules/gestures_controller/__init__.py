"""
    **Description**:
        module for customization gesture recognition process

    ----

    **Private Methods**:
        *__init__* --> initializes util

        *__get_gesture_path* --> returns gesture path

        *__check_for_gesture* --> checks if gesture exists
        
        *__check_for_hands* --> checks if hand(s) landmarks received

        *__process* --> process image to get hand(s) landmarks and recognition results

        *__gesture_received* --> sets current gesture

        *__image_received* --> saves image

    ----

    **Public Methods**:
        *start_recognition* --> starts recognizing gesture

        *stop_recognition* --> stops recognizing gesture

        *get_gesture* --> returns current gesture

        *get_hands* --> returns hand(s) landmarks

        *add_gesture* --> adds new gesture to datasets

        *remove_gesture* --> removes gesture from datasets

        *replace_gesture* --> replaces old gesture images with new one

        *retrain_model* --> retrains and exports model
"""

# initialize libraries
import os, numpy

# initialize modules
from src.modules.gestures_controller.hand_detector import HandDetector
from src.modules.gestures_controller.model_trainer import ModelTrainer
from src.modules.gestures_controller.gesture_recognizer import GestureRecognizer

from src.utils.open_cv.save_image import save
from src.utils.open_cv.frame_timestamp import calculate

from src.utils.open_cv.video_capture import VideoCapture

from src.utils.other.cleanup import Cleanup

# paths
path_to_models = os.path.abspath('models')
path_to_datasets = os.path.abspath('datasets')

class Gestures:
    @staticmethod
    def __get_gesture_path(name: str):
        # return 'path: str' to gesture 'directory'
        return os.path.join(path_to_datasets, name)

    def __check_for_gesture(self, name: str):
        # check if 'str' type received
        assert (type(name) == str)

        # get 'path: str'
        path_to_gesture = self.__get_gesture_path(name)

        # return 'true' if 'path_to_gesture: str' exists, otherwise 'false'
        return os.path.exists(path_to_gesture)

    def __check_for_hands(self, image: numpy.ndarray):
        # process 'image: ndarray' to check for 'hand(s)'
        processed_image = self.HandDetector.process(image)

        # get 'multi_hand_landmarks'
        self.multi_hand_landmarks = processed_image.multi_hand_landmarks

        # return 'true' if 'multi_hand_landmarks' received, otherwise 'false'
        return self.multi_hand_landmarks is not None

    def __process(self, image: numpy.ndarray):
        # clone 'image: ndarray'
        new_image = image.__copy__()

        # check for 'multi_hand_landmarks' in 'ndarray'
        if self.__check_for_hands(image):
            # calculate 'frame timestamp ms: int'
            frame_timestamp_ms = calculate(self.VideoCapture.capture)

            # process 'new_image: ndarray' to get recognition results
            self.GestureRecognizer.process(
                image=new_image,
                frame_timestamp_ms=frame_timestamp_ms
            )

    def __gesture_received(self, *args):
        # check if 'gestures' received
        results = args[0]

        if not results.gestures:
            return

        # set 'current gesture'
        self._CurrentGesture = results.gestures[0][0].category_name

    def __image_received(self, image: numpy.ndarray):
        # clone 'image: ndarray'
        new_image = image.__copy__()

        # check for 'multi_hand_landmarks' in 'ndarray'
        if self.__check_for_hands(new_image):
            # count 'image: ndarray'
            self._order += 1

            # save 'image: ndarray' as '.jpg' file
            save(
                image=image,
                index=self._order,
                gesture_name=self._gesture_name
            )

    def __init__(self, max_hands=2):
        # create hand detector with properties
        self.HandDetector = HandDetector(max_hands)

        # create model trainer
        self.ModelTrainer = ModelTrainer()

        # create gesture recognizer with 'gesture received: function'
        self.GestureRecognizer = GestureRecognizer(self.__gesture_received)

        # create video capture
        self.VideoCapture = VideoCapture()

        # last shown 'gesture'
        self._current_gesture = 'None'

        # empty variables
        self._order = None
        self._gesture_name = None

    def start_recognition(self):
        # start 'video capture'
        self.VideoCapture.start(self.__process)

    def stop_recognition(self):
        # stop 'video capture'
        self.VideoCapture.stop()

    def get_gesture(self):
        # check if 'video capture' is running
        if self.VideoCapture.running():
            # return 'current gesture: str'
            return self._current_gesture

    def get_hands(self):
        # check if 'video capture' is running
        if self.VideoCapture.running():
            # return 'multi_hand_landmarks'
            return self.multi_hand_landmarks

    def add_gesture(self, name: str):
        # check if 'multi_hand_landmarks' received
        if self.__check_for_gesture(name):
            return

        # create new 'directory' in 'datasets'
        os.makedirs(self.__get_gesture_path(name))

        # reset 'image: ndarray' count
        self._order = 0

        # reset gesture 'directory' name
        self._gesture_name = name

        # start 'video capture'
        self.VideoCapture.start(self.__image_received)

    def remove_gesture(self, name: str):
        # check if 'multi_hand_landmarks' received
        if self.__check_for_gesture(name):
            # delete gesture 'directory'
            Cleanup.delete_directory(self.__get_gesture_path(name))

    def replace_gesture(self, name: str):
        # remove old gesture
        self.remove_gesture(name)

        # add new gesture with the same 'name: str'
        self.add_gesture(name)

    def retrain_model(self):
        # cleanup 'models'
        Cleanup.clean_directory(path_to_models)

        # train 'model'
        self.ModelTrainer.train()

        # calculate 'loss: int' and 'accuracy: int' of 'model'
        loss, accuracy = self.ModelTrainer.get_accuracy()

        # check if 'accuracy: int' satisfied
        assert(accuracy < 80)

        # export 'model' as '.task' file
        self.ModelTrainer.export()