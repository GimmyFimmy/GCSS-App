from src.libs.communicator.solutions.registry import Registry
from src.utils.create import Create

class DevicesManager:
    def __init__(self, on_button_pressed):
        self.callback = on_button_pressed

        self.registry = Registry()

    def create(self):
        self.window = Create.window('400x440')
        self.canvas = Create.canvas(self.window, 440, 400)

        self.image_image_1 = Create.image(1, "image_1")
        self.image_image_2 = Create.image(1, "image_2")
        self.button_image_1 = Create.image(1, "button_1")
        self.button_image_2 = Create.image(1, "button_2")

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
            "Управление устройствами",
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

        count = 0
        devices = Registry.get_devices()

        for data in devices:
            port = data[1]
            name = data[2]

            distance = (count * 100)

            Create.frame(
                self.canvas,
                200.0,
                90.0+distance,
                self.image_image_2
            )

            Create.label(
                self.canvas,
                32.0,
                76.0+distance,
                name,
                24
            )

            Create.label(
                self.canvas,
                188.0,
                82.0+distance,
                port,
                16
            )

            button_1 = Create.button(
                self.button_image_1,
                280.0,
                75.0+distance,
                90.0,
                30.0,
            )

            button_1.configure(command=lambda button=port: self.callback(3, button))

            count += 1

        self.window.mainloop()

    def destroy(self):
        self.window.destroy()