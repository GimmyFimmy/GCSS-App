from src.utils.path import Path

# paths
MODEL_PATH = Path.get_path_to('model')
UTILS_PATH = Path.get_path_to('utils')
DATASETS_PATH = Path.get_path_to('datasets')
SOLUTIONS_PATH = Path.get_path_to('solutions')

ASSET_PATH = Path.get_path_to('gesture_recognizer.task', MODEL_PATH)

# 'hand_detector' properties
MAX_HANDS = 2
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

# 'model_trainer' properties
MIN_ACCURACY_PERCENTAGE = 70
MAX_ACCURACY_PERCENTAGE = 100

# 'gesture_recognizer' properties
DEFAULT_GESTURE = 'none'