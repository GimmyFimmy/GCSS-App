import os

from src.utils.create import Create

from src.constants import (
    Path,
    DATASETS_PATH
)

class GesturesManager:
    def __init__(self, on_button_pressed, on_remove_gesture_pressed):
        self.callback = on_button_pressed
        self.remove = on_remove_gesture_pressed

    def create(self):
        self.window = Create.window(400, 440)
        self.canvas = Create.canvas(self.window, 440, 400)

        self.image_image_1 = Create.image(2, "image_1")
        self.image_image_2 = Create.image(2, "image_2")
        self.button_image_1 = Create.image(2, "button_1")
        self.button_image_2 = Create.image(2, "button_2")
        self.button_image_3 = Create.image(2, "button_3")

        Create.frame(
            self.canvas,
            200.0,
            220.0,
            self.image_image_1
        )

        Create.label(
            self.canvas,
            92.0,
            8.0,
            "Управление жестами",
            20
        )

        Create.button(
            self.button_image_2,
            12.0,
            0.0,
            40.0,
            40.0,
            lambda: self.callback(0)
        )

        Create.button(
            self.button_image_3,
            350.0,
            0.0,
            40.0,
            40.0,
            lambda: self.callback(3, False)
        )

        count = 0
        gestures = os.listdir(DATASETS_PATH)

        for directory in gestures:
            distance = (count * 80)

            Create.frame(
                self.canvas,
                200.0,
                80.0+distance,
                self.image_image_2
            )

            Create.button(
                self.button_image_1,
                280.0,
                65.0+distance,
                90.0,
                30.0,
                lambda name=directory: self.remove(name)
            )

            Create.label(
                self.canvas,
                34.0,
                66.0+distance,
                directory,
                24
            )

            Create.label(
                self.canvas,
                194.0,
                74.0+distance,
                "~мб",
                16
            )

            count += 1

        self.window.mainloop()