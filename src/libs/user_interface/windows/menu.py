import time, datetime

from src.utils.create import Create

from src.constants import (
    UPDATE_DELAY,
    WEEKDAYS
)

class Menu:
    def __init__(self, on_button_pressed, on_display_info_pressed):
        self.callback = on_button_pressed
        self.display = on_display_info_pressed

        self.time = None
        self.date = None
        self.weather = None

    def create(self, *args):
        self.window = Create.window(1000, 600)
        self.canvas = Create.canvas(self.window, 600, 1000)

        self.image_image_1 = Create.image(0, "image_1")
        self.image_image_2 = Create.image(0, "image_2")
        self.button_image_1 = Create.image(0, "button_1")
        self.button_image_2 = Create.image(0, "button_2")
        self.button_image_3 = Create.image(0, "button_3")

        def update():
            current_time = time.strftime('%H:%M')

            date = datetime.date.today()
            weekday = WEEKDAYS[datetime.date.weekday(date)]

            self.canvas.itemconfig(tagOrId=self.time, text=current_time)
            self.canvas.itemconfig(tagOrId=self.date, text=f'{weekday}.\n{date.day}')

            self.window.after(UPDATE_DELAY, update)

        Create.frame(
            self.canvas,
            500.0,
            300.0,
            self.image_image_1
        )

        Create.frame(
            self.canvas,
            335.0,
            520.0,
            self.image_image_2
        )

        Create.button(
            self.button_image_1,
            475.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(1, False),
        )

        Create.button(
            self.button_image_2,
            585.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(2)
        )

        Create.button(
            self.button_image_3,
            695.0,
            475.0,
            90.0,
            90.0,
            lambda: self.display()
        )

        self.time = Create.label(
            self.canvas,
            313.0,
            63.0,
            '',
            128
        )

        self.date = Create.label(
            self.canvas,
            253.0,
            486.0,
            '',
            28
        )

        self.weather = Create.label(
            self.canvas,
            364.0,
            503.0,
            '~~°C',
            28
        )

        update()

        self.window.mainloop()