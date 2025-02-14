from src.utils.create import Create

class GestureName:
    def __init__(self, on_button_pressed, on_save_button_pressed):
        self.callback = on_button_pressed
        self.save = on_save_button_pressed

    def create(self, *args):
        self.window = Create.window(300, 200)
        self.canvas = Create.canvas(self.window, 200, 300)

        self.image_image_1 = Create.image(3, "image_1")
        self.image_image_2 = Create.image(3, "image_2")
        self.button_image_1 = Create.image(3, "button_1")
        self.button_image_2 = Create.image(3, "button_2")

        Create.frame(
            self.canvas,
            150.0,
            100.0,
            self.image_image_1
        )

        Create.button(
            self.button_image_2,
            12.0,
            0.0,
            40.0,
            40.0,
            lambda: self.callback(1, False)
        )

        Create.label(
            self.canvas,
            64.0,
            9.0,
            'Добавление жеста',
            18
        )

        Create.frame(
            self.canvas,
            150.0,
            100.0,
            self.image_image_2
        )

        self.entry = Create.input_box(
            50.0,
            75.0,
            200.0,
            48.0,
        )

        Create.button(
            self.button_image_1,
            90.0,
            160.0,
            120.0,
            30.0,
            lambda: self.save(self.entry.get())
        )

        self.window.mainloop()