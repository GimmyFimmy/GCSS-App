from src.lib.gesture_recognizer.constants import MAX_ACCURACY_PERCENTAGE

def calculate(accuracy: int):
    return round(accuracy * MAX_ACCURACY_PERCENTAGE)