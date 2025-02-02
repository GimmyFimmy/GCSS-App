"""
    **Description**:
        module for customization gesture recognition process

    ----

    **Utils Methods**
        *get_gesture_path* --> returns gesture path

        *check_for_gesture* --> checks if gesture folder exists

        *save_image* --> saves image

        *calculate_frame_timestamp* --> calculates frame timestamp in ms

    ----

    **Private Methods**:
        *__init__* --> initializes util
        
        *__check_for_hands* --> checks if hand(s) landmarks received

        *__recognize_process* --> process image to get hand(s) landmarks and recognition results

        *__save_process* --> process image to save it

    ----

    **Public Methods**:
        *start_recognition* --> starts recognizing gesture

        *stop_recognition* --> stops recognizing gesture

        *get_hands* --> returns hand(s) landmarks

        *add_gesture* --> adds new gesture to datasets

        *remove_gesture* --> removes gesture from datasets

        *train_model* --> trains and exports model
"""

# initialize libraries
import os, numpy, cv2

# initialize modules
from src.modules.gestures_controller.hand_detector import HandDetector
from src.modules.gestures_controller.model_trainer import ModelTrainer
from src.modules.gestures_controller.gesture_recognizer import GestureRecognizer

# initialize utils
from src.utils.video_capture import VideoCapture
from src.utils.cleanup import Cleanup
from src.utils.logger import Logger

# paths
path_to_models = os.path.abspath('models')
path_to_datasets = os.path.abspath('datasets')

#variables
MAX_HANDS = 2

MAX_SAVED_IMAGE = 100

MIN_ACCURACY_PERCENTAGE = 80
MAX_ACCURACY_PERCENTAGE = 100

# create utils and modules
VideoCapture = VideoCapture()
Logger = Logger('gestures_controller')

GestureRecognizer = GestureRecognizer() # NOTE: this module must be created first, otherwise a RuntimeError will be thrown
HandDetector = HandDetector(MAX_HANDS)
ModelTrainer = ModelTrainer()

class Utils:
    @staticmethod
    def get_gesture_path(name: str):
        # check if 'str' type received
        Logger.assertion(type(name) is str, '<name> must be string!')

        # return 'path: str' to gesture 'directory'
        return os.path.join(path_to_datasets, name)

    @staticmethod
    def check_for_gesture(name: str):
        # get 'path: str'
        path_to_gesture = Utils.get_gesture_path(name)

        # return 'true' if 'path_to_gesture: str' exists, otherwise 'false'
        return os.path.exists(path_to_gesture)

    @staticmethod
    def save_image(image: numpy.ndarray, gesture_name: str, index: int):
        # try to save 'image: ndarray'
        try:
            # save 'image: ndarray' as '.jpg' file
            return cv2.imwrite(
                filename=path_to_datasets + f'/{gesture_name}/{str(index)}.jpg',
                img=image
            )
        except Exception as result:
            # raise warning
            Logger.warning(f'failed to save image. Message: {result}')

    @staticmethod
    def calculate_frame_timestamp():
        # return 'frame timestamp ms: int'
        return int(VideoCapture.capture.get(cv2.CAP_PROP_POS_MSEC))

class GesturesController:
    def __check_for_hands(self, image: numpy.ndarray):
        # process 'image: ndarray' to check for 'hand(s)'
        processed_image = HandDetector.process(image)

        # get 'multi_hand_landmarks'
        self.multi_hand_landmarks = processed_image.multi_hand_landmarks

        # return 'true' if 'multi_hand_landmarks' received, otherwise 'false'
        return self.multi_hand_landmarks is not None

    def __recognize_process(self, image: numpy.ndarray):
        # clone 'image: ndarray'
        new_image = image.__copy__()

        # check for 'multi_hand_landmarks' in 'ndarray'
        if self.__check_for_hands(new_image):
            # calculate 'frame timestamp ms: int'
            frame_timestamp_ms = Utils.calculate_frame_timestamp()

            # process 'new_image: ndarray' to get recognition results
            GestureRecognizer.process(
                image=new_image,
                frame_timestamp_ms=frame_timestamp_ms
            )

            HandDetector.draw(new_image, self.multi_hand_landmarks)

        cv2.imshow('test', new_image)

    def __save_process(self, image: numpy.ndarray):
        # clone 'image: ndarray'
        new_image = image.__copy__()

        # check for 'multi_hand_landmarks' in 'ndarray'
        if self.__check_for_hands(new_image):
            # count 'image: ndarray'
            self.__order += 1

            # save 'image: ndarray' as '.jpg' file
            Utils.save_image(
                image=image,
                index=self.__order,
                gesture_name=self.__name
            )

        # check if 'order: int' is equal 100
        if self.__order == MAX_SAVED_IMAGE:
            # stop 'video capture'
            VideoCapture.stop()

    def __init__(self, gesture_changed: ()):
        # check if 'function' type received
        Logger.assertion(callable(gesture_changed), '<gesture_changed> must be function!')

        # set gesture recognizer 'listener: function'
        GestureRecognizer.set_listener(gesture_changed)

        # empty variables
        self.__order = None
        self.__name = None

        # debug that 'controller' initialized
        Logger.debug('initialized')

    def start_recognition(self):
        # debug that 'gesture' recognition begin
        Logger.debug('recognition began')

        # start 'video capture'
        VideoCapture.start(self.__recognize_process)

    def stop_recognition(self):
        # debug that 'gesture' recognition ended
        Logger.debug('recognition ended')

        # stop 'video capture'
        VideoCapture.stop()

    def get_hands(self):
        # check if 'video capture' is running
        if VideoCapture.is_running():
            # return 'multi_hand_landmarks'
            return self.multi_hand_landmarks

    def add_gesture(self, name: str):
        # check if 'multi_hand_landmarks' received
        if Utils.check_for_gesture(name):
            # warn that 'gesture' already exists
            Logger.warning(f'gesture {name} already exists')
            return

        # debug that new 'gesture' is going to be added
        Logger.debug(f'adding new gesture with name {name}')

        # create new 'directory' in 'datasets'
        os.makedirs(Utils.get_gesture_path(name))

        # reset 'order: int' and gesture 'name: str'
        self.__order = 0
        self.__name = name

        # start 'video capture'
        VideoCapture.start(self.__save_process)

    def remove_gesture(self, name: str):
        # check if 'name: str' received
        if Utils.check_for_gesture(name):
            # debug that new 'gesture' is going to be removed
            Logger.debug(f'removing gesture with name {name}')

            # delete gesture 'directory'
            Cleanup.delete_directory(Utils.get_gesture_path(name))

    def train_model(self):
        # debug that 'model' is going to be retrained
        Logger.debug(f'training model')

        # cleanup 'models'
        Cleanup.clean_directory(path_to_models)

        # train 'model'
        ModelTrainer.train()

        # calculate 'loss: int' and 'accuracy: int' of 'model'
        loss, accuracy = ModelTrainer.get_accuracy()

        # rounding 'accuracy: int'
        accuracy_percentage = round(accuracy * MAX_ACCURACY_PERCENTAGE)

        # check if 'accuracy: int' satisfied
        if accuracy_percentage <= MIN_ACCURACY_PERCENTAGE:
            # warn that 'accuracy' is lower than 80%
            Logger.warning(f'model accuracy is lower than expected: {accuracy_percentage}%')

        # export 'model' as '.task' file
        ModelTrainer.export()

        # debug that 'model' trained
        Logger.debug(f'model trained')