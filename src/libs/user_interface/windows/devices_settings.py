import customtkinter

from customtkinter import *

from src.libs.communicator.solutions.registry import Registry
from src.constants import (
    DATASETS_PATH
)

class DevicesSettings:
    def __init__(self):
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        self.window = CTk()
        self.window.resizable(False, False)
        self.window.geometry(400, 440)

        self.frame = CTkScrollableFrame(
            self.window,
            orientation='vertical',
            width=400,
            height=440,
            label_text='Редактирование устройства',
            label_font=('', 20)
        )
        self.frame.pack()

    def create(self, port: str):
        data = Registry.read_device(port)
        gestures = os.listdir(DATASETS_PATH)

        def on_button_pressed(*args):
            print(args)

        if data is not None:
            CTkLabel(self.frame, text=f'IP-Адрес: {data[0]}', fg_color='transparent').pack()
            CTkLabel(self.frame, text=f'Порт: {data[1]}', fg_color='transparent').pack(pady=20)

            for line in data[3:]:
                key, value = line.split('=')

                CTkLabel(self.frame, text=f'{key}', fg_color='transparent').pack(pady=10)

                option_menu = CTkOptionMenu(self.frame, values=gestures)
                option_menu.set(value)
                option_menu.configure(command=on_button_pressed)
                option_menu.pack()

        self.window.mainloop()