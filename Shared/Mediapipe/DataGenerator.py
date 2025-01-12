import cv2
import os.path

from Shared.OpenCV import  VideoCapture
from Shared.Mediapipe import HandDetector
from Shared.Utils.DirectoriesManager import DirectoriesManager

path_to_datasets = os.path.abspath('Datasets')

images_limit = 99

class DataGenerator():
    def __init__(self):
        self.VideoCapture = VideoCapture.VideoCapture(
            display_video=True,
            display_name="Capturing images..."
        )

        self.HandDetector = HandDetector.HandDetector(
            max_hands=2,
            draw_landmarks=True
        )

    def __get_directory(self, name: str):
        assert(type(name) == str)

        self._gesture_name = name

        if name == "None":
            print("can't return folder with given name 'None'!")
            return

        if os.path.exists(path_to_datasets+f'/{name}'):
            return path_to_datasets+f'/{name}'

    def __generate_dataset(self, name: str):
        self._index = 0
        self.VideoCapture.start_capture(self.__on_frame_changed)

    def __on_frame_changed(self, image):
        if self._index == images_limit:
            self.VideoCapture.stop_capture()
            return

        result = self.HandDetector.process(image)

        if result.multi_hand_landmarks:
            cv2.imwrite(
                filename=path_to_datasets+f'/{self._gesture_name}/{str(self._index)}.jpg',
                img=image
            )

            self._index += 1

    def add_gesture(self, name: str):
        if self.__get_directory(name):
            print("folder already exists!")
            return

        DirectoriesManager.create_directory(path_to_datasets+f'/{name}')

        self.__generate_dataset(name)

    def change_gesture(self, name: str):
        path_to_directory = self.__get_directory(name)

        if path_to_directory:
            DirectoriesManager.delete_content(path_to_directory)

            self.__generate_dataset(name)

    def delete_gesture(self, name: str):
        path_to_directory = self.__get_directory(name)
        DirectoriesManager.delete_directory(path_to_directory)

a=DataGenerator()
a.add_gesture("fuck")