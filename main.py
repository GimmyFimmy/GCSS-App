import os

from threading import Thread

from src.libs.communicator import *
from src.libs.user_interface import *
from src.libs.gesture_recognizer import *
from src.libs.user_interface.windows.devices_settings import DevicesSettings

from src.utils import (
    calculate,
    ip_address,
    video_capture,
    draw_landmarks,
    create
)

from src.constants import (
    Path,
    DATASETS_PATH,
    DEFAULT_GESTURE
)

class App:
    def __check_for_hands(self, image):
        # process 'image: ndarray' to check for 'hand(s)'
        processed_image = self.hand_detector.process(image)

        # get 'multi_hand_landmarks'
        self.multi_hand_landmarks = processed_image.multi_hand_landmarks

        # return 'true' if 'multi_hand_landmarks' received, otherwise 'false'
        return self.multi_hand_landmarks is not None

    def __process_recognition(self, image):
        # clone 'image: ndarray'
        new_image = image.__copy__()

        # check for 'multi_hand_landmarks' in 'ndarray'
        if self.__check_for_hands(new_image):
            # calculate 'frame timestamp ms: int'
            frame_timestamp_ms = calculate.frame_timestamp(self.video_capture.capture)

            # process 'new_image: ndarray' to get recognition results
            self.gesture_recognizer.process(
                image=new_image,
                frame_timestamp_ms=frame_timestamp_ms
            )

    def __process_saving(self, image):
        pass

    def __on_gesture_received(self, gesture: str):
        if gesture != DEFAULT_GESTURE:
            for data in self.registry.get_devices():
                keys = ""

                for line in data[3:]:
                    key, value = line.split('=')

                    if value == gesture:
                        keys += f"{key}_"

                if len(keys) != 0:
                    address = (data[0], int(data[1]))

                    self.communicator.send(address, keys)

    def __from_client_received(self, data, address):
        if not self.registry.get_device(address):
            self.create.box(0, 'Уведомление', 'Новое умное устройство было обнаружено!')

            self.registry.write_device(address, data)
            self.communicator.send(address, 'ps')

    def __on_button_pressed(self, index: int, *args):
        self.current_window.destroy()

        self.current_window = self.windows[index]
        self.current_window.create(*args)

    def __on_add_gesture_pressed(self):
        self.create.box(0, 'Информация', '''
        Следуйте указаниям ниже:
        
         1. Включите свет в помещении
         
         2. Держите руку напротив обьектива камеры
         
         3. Не меняйте жест руки
        ''')

        self.count = 0

    def __on_remove_gesture_pressed(self, name: str):
        box = self.create.box(2, 'Предупреждение', 'Вы уверены, что хотите удалить жест?')

        if box:
            gesture_path = Path.get_path_to(name, DATASETS_PATH)

            Path.remove_directory(gesture_path)

            self.current_window.destroy()
            self.current_window.create()

    def __init__(self):
        self.registry = Registry()
        self.communicator = Communicator(self.__from_client_received)

        self.gesture_recognizer = GestureRecognizer(self.__on_gesture_received)
        #self.model_trainer = ModelTrainer()
        self.hand_detector = HandDetector()

        self.create = create.Create()
        self.video_capture = video_capture.VideoCapture()

        self.windows = [
            Menu(self.__on_button_pressed),
            GesturesManager(self.__on_button_pressed, self.__on_add_gesture_pressed, self.__on_remove_gesture_pressed),
            DevicesManager(self.__on_button_pressed)
        ]

        DevicesSettings().create('9999')

        self.communicator_thread = Thread(target=self.communicator.start)
        self.video_capture_thread = Thread(target=lambda: self.video_capture.start(self.__process_recognition))

        self.communicator_thread.start()
        self.video_capture_thread.start()

        #self.create.box(0, 'Информация', f'IP-адрес станции: {ip_address.get()}')

        #self.current_window = self.windows[0]
        #self.current_window.create()

if __name__ == "__main__":
    App()