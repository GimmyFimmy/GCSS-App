# import libraries
from tkinter import messagebox

from src.utils.path import Path

# paths
UTILS_PATH = 'src/utils'
ASSETS_PATH = 'src/libs/user_interface/assets'

DEVICES_PATH = 'src/libs/communicator/devices'
MODEL_PATH = 'src/libs/gesture_recognizer/model'
DATASETS_PATH = 'src/libs/gesture_recognizer/datasets'

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

# 'communicator' properties
LOCAL_PORT = 8888
BUFFER_SIZE = 1024

# 'menu' properties
UPDATE_DELAY = 1000
WEEKDAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг','Пятница', 'Суббота', 'Воскресенье',]

# 'create' properties
BOXES_TYPES = [messagebox.showinfo, messagebox.showwarning, messagebox.askyesno, messagebox.showerror]

# 'main' properties
MAX_IMAGES = 100