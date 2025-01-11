import os.path
import mediapipe_model_maker

from mediapipe_model_maker import image_classifier

from Shared.Mediapipe.DataGenerator import path_to_datasets
from Shared.Utils.DirectoriesManager import DirectoriesManager

path_to_models = os.path.abspath('Models')

class ModelTrainer():
    def __init__(self):
        self.data = image_classifier.Dataset.from_folder(path_to_datasets)
        self.supported_model = image_classifier.SupportedModels.MOBILENET_V2

        self.hparams = image_classifier.HParams(
            export_dir=path_to_models
        )

        self.options = image_classifier.ImageClassifierOptions(
            supported_model=self.supported_model,
            hparams=self.hparams
        )

    def __check_for_model(self):
        if not self.model:
            print("no model was detected!")

        return self.model != None

    def train_model(self):
        train_data, remaining_data = self.data.split(0.8)
        self.test_data, validation_data = remaining_data.split(0.5)

        self.model = image_classifier.ImageClassifier.create(
            train_data=train_data,
            validation_data=validation_data,
            options=self.options,
        )

    def get_model_accuracy(self):
        if not self.__check_for_model():
            return

        return self.model.evaluate(self.test_data)

    def export_model(self, name="model"):
        if not self.__check_for_model():
            return

        self.model.export_model(model_name=name+'.tfile')

    def destroy_all_models(self):
        DirectoriesManager.delete_content(path_to_models)