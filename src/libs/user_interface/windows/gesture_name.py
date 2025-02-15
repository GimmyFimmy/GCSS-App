from src.utils.create import Create

class GestureName:
    def __init__(self, on_button_pressed, on_save_pressed):
        self.save = on_save_pressed
        self.callback = on_button_pressed

    def create(self):
        self.window = Create.window(400, 250)
        self.canvas = Create.canvas(self.window, 250, 400)

        self.image_image_1 = Create.image(2, "image_1")
        self.button_image_1 = Create.image(2, "button_1")
        self.button_image_2 = Create.image(2, "button_2")

        Create.frame(
            self.canvas,
            200.0,
            125.0,
            self.image_image_1
        )

        Create.button(
            self.button_image_1,
            10.0,
            170.0,
            180.0,
            70.0,
            lambda: self.save(self.entry.get())
        )

        Create.button(
            self.button_image_2,
            210.0,
            170.0,
            180.0,
            70.0,
            lambda: self.callback(1)
        )

        self.entry = Create.input_box(
            15.0,
            70.0,
            370.0,
            68.0
        )

        self.window.mainloop()