import os.path
import mediapipe_model_maker

from mediapipe_model_maker import gesture_recognizer

from Shared.Mediapipe.DataGenerator import path_to_datasets
from Shared.Utils.DirectoriesCleanup import DirectoriesCleanup

path_to_models = os.path.abspath('Models')

class ModelTrainer():
    def __init__(self):
        self.data = data = gesture_recognizer.Dataset.from_folder(
            dirname=path_to_datasets,
            hparams=gesture_recognizer.HandDataPreprocessingParams()
        )

        self.hparams = gesture_recognizer.HParams(
            export_dir=path_to_models
        )

        self.options = gesture_recognizer.GestureRecognizerOptions(
            hparams=self.hparams
        )

    def __check_for_model(self):
        if self.model == None:
            print("no model was detected!")

        return self.model != None

    def train_model(self):
        train_data, remaining_data = self.data.split(0.8)
        self.test_data, validation_data = remaining_data.split(0.5)

        self.model = gesture_recognizer.GestureRecognizer.create(
            train_data=train_data,
            validation_data=validation_data,
            options=self.options,
        )

    def get_model_accuracy(self):
        if not self.__check_for_model():
            return

        return self.model.evaluate(self.test_data, batch_size=1)

    def export_model(self):
        if not self.__check_for_model():
            return

        self.model.export_model()

    def destroy_all_models(self):
        DirectoriesCleanup.delete_content(path_to_models)