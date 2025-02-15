import os

from src.utils.create import Create

from src.constants import (
    DATASETS_PATH
)

class GesturesEditor:
    def __init__(self, on_button_pressed, on_remove_gesture_pressed, on_retrain_pressed):
        self.callback = on_button_pressed
        self.retrain = on_retrain_pressed
        self.remove = on_remove_gesture_pressed

    def create(self):
        self.window = Create.window(1000, 600)
        self.canvas = Create.canvas(self.window, 600, 1000)

        self.image_image_1 = Create.image(1, "image_1")
        self.image_image_2 = Create.image(1, "image_2")
        self.image_image_3 = Create.image(1, "image_4")
        self.button_image_1 = Create.image(1, "button_1")
        self.button_image_2 = Create.image(1, "button_2")
        self.button_image_3 = Create.image(1, "button_3")
        self.button_image_4 = Create.image(1, "button_5")

        Create.frame(
            self.canvas,
            500.0,
            300.0,
            self.image_image_1
        )

        Create.button(
            self.button_image_1,
            35.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(0)
        )

        Create.button(
            self.button_image_2,
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(3, False)
        )

        Create.button(
            self.button_image_3,
            795.0,
            35.0,
            70.0,
            70.0,
            self.retrain
        )

        count = 0
        gestures = os.listdir(DATASETS_PATH)

        for file in gestures:
            if file == 'None':
                continue

            count += 1
            x_distance = 500 if count > 3 else 0
            y_distance = (165 * (count - 4)) if count > 3 else (165 * (count - 1))

            Create.frame(
                self.canvas,
                250.0+x_distance,
                195.0+y_distance,
                self.image_image_2
            )

            Create.label(
                self.canvas,
                136.0+x_distance,
                173.0+y_distance,
                file,
                36
            )

            Create.button(
                self.button_image_4,
                285.0+x_distance,
                160.0+y_distance,
                180.0,
                70.0,
                lambda data=file: self.remove(data)
            )

            Create.frame(
                self.canvas,
                70.0+x_distance,
                195.0+y_distance,
                self.image_image_3
            )

        Create.label(
            self.canvas,
            290.0,
            46.0,
            'Управление жестами',
            40
        )

        self.window.mainloop()