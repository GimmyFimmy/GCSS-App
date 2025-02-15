from tkinter import *

from src.constants import (
    Path,
    ASSETS_PATH,
    BOXES_TYPES
)

from src.utils.calculate import screen_center

class Create:
    @staticmethod
    def window(width: int, height: int):
        window = Tk()

        x, y = screen_center(window, width, height)

        window.geometry(f'{width}x{height}+{x}+{y}')
        window.resizable(False, False)

        window.focus_force()

        return window

    @staticmethod
    def canvas(window, height: float, width: float):
        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=height,
            width=width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        return canvas

    @staticmethod
    def label(canvas, x: float, y: float, text: str, point: int):
         label = canvas.create_text(
            x,
            y,
            anchor="nw",
            text=text,
            fill="#FFFFFF",
            font=("Inter Bold", point * -1)
         )

         return label

    @staticmethod
    def image(index: int, image: str):
        image_path = ASSETS_PATH + f'/frame{index}/{image}.png'

        if Path.exists(image_path):
            return PhotoImage(
                file=image_path
            )

    @staticmethod
    def frame(canvas, x: float, y: float, image):
        frame = canvas.create_image(
            x,
            y,
            image=image
        )

        return frame

    @staticmethod
    def button(image, x: float, y: float, w: float, h: float, callback=None, text=None):
        button = Button(
            image=image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=callback,
            text=text,
        )

        button.place(
            x=x,
            y=y,
            width=w,
            height=h
        )

        return button

    @staticmethod
    def box(category: int, title: str, text: str):
        dialogue_box = BOXES_TYPES[category]

        if dialogue_box is not None:
            box = dialogue_box(
                title,
                text
            )

            return box

    @staticmethod
    def input_box(x: float, y: float, width: float, height: float):
        input = Entry(
            bd=0,
            bg="#404040",
            fg="#FFFFFF",
            highlightthickness=0,
            font=('Inter Bold', 30)
        )

        input.place(
            x=x,
            y=y,
            width=width,
            height=height,

        )

        return input