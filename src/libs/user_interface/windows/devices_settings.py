from src.libs.communicator.solutions.registry import Registry
from src.utils.create import Create

class DevicesSettings:
    def __init__(self, on_button_pressed, on_save_pressed):
        self.callback = on_button_pressed
        self.save = on_save_pressed

        self.registry = Registry()

    def create(self, data):
        self.window = Create.window(1000, 600)
        self.canvas = Create.canvas(self.window, 600, 1000)

        self.image_image_1 = Create.image(1, "image_1")
        self.image_image_2 = Create.image(1, "image_2")
        self.image_image_3 = Create.image(1, "image_5")
        self.button_image_1 = Create.image(1, "button_1")
        self.button_image_2 = Create.image(1, "button_6")
        self.button_image_3 = Create.image(1, "button_3")

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
            lambda: self.callback(2)
        )

        Create.button(
            self.button_image_3,
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.save(data, self.input_data)
        )

        self.count = 0
        self.input_data = {}

        for line in data[3:]:
            key, value = line.split('=')

            self.count += 1

            x_distance = 500 if self.count > 3 else 0
            y_distance = (165 * (self.count - 4)) if self.count > 3 else (165 * (self.count - 1))

            Create.frame(
                self.canvas,
                250.0 + x_distance,
                195.0 + y_distance,
                self.image_image_2
            )

            Create.label(
                self.canvas,
                136.0 + x_distance,
                173.0 + y_distance,
                key,
                36
            )

            Create.frame(
                self.canvas,
                375.0 + x_distance,
                195.0 + y_distance,
                self.button_image_2,
            )

            input = Create.input_box(
                290 + x_distance,
                165 + y_distance,
                170,
                60
            )

            input.insert(0, value)

            self.input_data[key] = input

            Create.frame(
                self.canvas,
                70.0 + x_distance,
                195.0 + y_distance,
                self.image_image_3
            )

        Create.label(
            self.canvas,
            340.0,
            46.0,
            f'Настройки {data[2]}',
            40
        )

        self.window.mainloop()