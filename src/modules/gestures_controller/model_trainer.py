"""
    **Description**:
        util for creating gesture recognition models

    ----

    **Private Methods**:
        *__init__* -> initializes util

    ----

    **Public Methods**:
        *train* -> returns model

        *get_accuracy* -> tests model to get accuracy and loss

        *export* -> creates a new model
"""

# import libraries
import os.path

from PIL.features import modules
from mediapipe_model_maker import gesture_recognizer

# paths
path_to_models = os.path.abspath('models')
path_to_datasets = os.path.abspath('datasets')

class ModelTrainer:
    def __init__(self):
        # create 'data' for model training
        self.data = gesture_recognizer.Dataset.from_folder(
            dirname=path_to_datasets,
            hparams=gesture_recognizer.HandDataPreprocessingParams()
        )

        # create 'parameters' for model
        self.hparams = gesture_recognizer.HParams(
            export_dir=path_to_models
        )

        # create 'options' for model
        self.options = gesture_recognizer.GestureRecognizerOptions(
            hparams=self.hparams
        )

        # empty variables
        self.model = None
        self.test_data = None
        self.train_data = None

    def train(self):
        # split 'data' on 'test data' and 'train data'
        self.train_data, remaining_data = self.data.split(0.8)
        self.test_data, validation_data = remaining_data.split(0.5)

        # create new 'model' with 'data', 'properties', 'options'
        self.model = gesture_recognizer.GestureRecognizer.create(
            train_data=self.train_data,
            validation_data=validation_data,
            options=self.options,
        )

    def get_accuracy(self):
        # check if 'model' exists
        assert(self.model is not None)

        # return model 'accuracy: int' and 'loss: int'
        return self.model.evaluate(self.test_data, batch_size=1)

    def export(self):
        # check if 'model' exists
        assert(self.model is not None)

        # export 'model' as '.task' file
        self.model.export_model()