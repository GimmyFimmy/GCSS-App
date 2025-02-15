from src.libs.communicator.solutions.registry import Registry
from src.utils.create import Create

class DevicesEditor:
    def __init__(self, on_button_pressed):
        self.callback = on_button_pressed

        self.registry = Registry()

    def create(self):
        self.window = Create.window(1000, 600)
        self.canvas = Create.canvas(self.window, 600, 1000)

        self.image_image_1 = Create.image(1, "image_1")
        self.image_image_2 = Create.image(1, "image_2")
        self.image_image_3 = Create.image(1, "image_3")
        self.button_image_1 = Create.image(1, "button_1")
        self.button_image_2 = Create.image(1, "button_2")
        self.button_image_3 = Create.image(1, "button_3")
        self.button_image_4 = Create.image(1, "button_4")

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

        count = 0
        devices = Registry.get_devices()

        for data in devices:
            name = data[2]

            count += 1

            x_distance = 500 if count > 3 else 0
            y_distance = (165 * (count - 4)) if count > 3 else (165 * (count - 1))

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
                name,
                36
            )

            Create.button(
                self.button_image_4,
                285.0 + x_distance,
                160.0 + y_distance,
                180.0,
                70.0,
                lambda device=data: self.callback(4, True, device)
            )

            Create.frame(
                self.canvas,
                70.0 + x_distance,
                195.0 + y_distance,
                self.image_image_3
            )

        Create.label(
            self.canvas,
            300.0,
            46.0,
            'Управление устройствами',
            40
        )

        self.window.mainloop()