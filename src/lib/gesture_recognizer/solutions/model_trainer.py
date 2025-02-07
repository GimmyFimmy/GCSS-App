"""
    **Description**:
        util for creating gesture recognition model

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
from mediapipe_model_maker import gesture_recognizer

from src.lib.gesture_recognizer.constants import (
    Path,
    MODEL_PATH,
    DATASETS_PATH
)

class ModelTrainer:
    def __init__(self, dataset='sample'):
        # get path to 'dataset: dir'
        self.dataset_path = Path.get_path_to(dataset, DATASETS_PATH)

        # create 'data' for model training
        self.data = gesture_recognizer.Dataset.from_folder(
            dirname=self.dataset_path,
            hparams=gesture_recognizer.HandDataPreprocessingParams()
        )

        # create 'parameters' for model
        self.hparams = gesture_recognizer.HParams(
            export_dir=MODEL_PATH
        )

        # create 'options' for model
        # NOTE: error may occur if 'dataset: dir' is empty or nil
        self.options = gesture_recognizer.GestureRecognizerOptions(
            hparams=self.hparams
        )

        # create empty variables
        self.model = None
        self.test_data = None
        self.train_data = None

    def train(self):
        # clean 'dataset'
        # NOTE: error may occur if 'model: dir' is not empty
        Path.clean_directory(MODEL_PATH)

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