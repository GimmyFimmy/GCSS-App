from tkinter import *

from src.constants import (
    Path,
    ASSETS_PATH,
    BOXES_TYPES
)

class Create:
    @staticmethod
    def window(geometry: str):
        window = Tk()
        window.geometry(geometry)
        window.resizable(False, False)

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
        image_path = ASSETS_PATH + f'/frame_{index}/{image}.png'

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
    def button(image, x: float, y: float, w: float, h: float, callback=None):
        button = Button(
            image=image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=callback
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
            return dialogue_box(
                title=title,
                message=text
            )