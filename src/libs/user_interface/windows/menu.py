import time, datetime

from src.utils.create import Create

from src.constants import (
    UPDATE_DELAY,
    WEEKDAYS
)

class Menu:
    def __init__(self, on_button_pressed):
        self.on_button_pressed = on_button_pressed

        self.time = None
        self.date = None

    def create(self, *args):
        self.window = Create.window(600, 360)
        self.canvas = Create.canvas(self.window, 360, 600)

        self.image_image_1 = Create.image(0, "image_1")
        self.image_image_2 = Create.image(0, "image_2")
        self.button_image_1 = Create.image(0, "button_1")
        self.button_image_2 = Create.image(0, "button_2")
        self.button_image_3 = Create.image(0, "button_3")

        def update_time():
            current_time = time.strftime('%H:%M')

            date = datetime.date.today()
            weekday = WEEKDAYS[datetime.date.weekday(date)]

            self.canvas.itemconfig(tagOrId=self.time, text=current_time)
            self.canvas.itemconfig(tagOrId=self.date, text=f'{weekday}, {date.day}')

            self.window.after(UPDATE_DELAY, update_time)

        Create.frame(
            self.canvas,
            300.0,
            180.0,
            self.image_image_1
        )

        self.time = Create.label(
            self.canvas,
            240.0,
            55.0,
            "",
            48
        )

        self.date = Create.label(
            self.canvas,
            255.0,
            115.0,
            "",
            14
        )

        Create.frame(
            self.canvas,
            300.0,
            320.0,
            self.image_image_2
        )

        Create.button(
            self.button_image_1,
            355.0,
            300.0,
            40.0,
            40.0,
            lambda: self.on_button_pressed(0),
        )

        Create.button(
            self.button_image_2,
            280.0,
            300.0,
            40.0,
            40.0,
            lambda: self.on_button_pressed(2, False)
        )

        Create.button(
            self.button_image_3,
            205.0,
            300.0,
            40.0,
            40.0,
            lambda: self.on_button_pressed(1, False)
        )

        update_time()

        self.window.mainloop()