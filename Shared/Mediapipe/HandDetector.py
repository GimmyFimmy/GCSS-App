import mediapipe

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils
from mediapipe.python.solutions import drawing_styles

class HandDetector():
    def __init__(self, max_hands=2, draw_landmarks=False):
        self.Hands = hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.draw_landmarks = draw_landmarks

    def process(self, image):
        assert (image.all() != None)

        results = self.Hands.process(image) or None

        if results.multi_hand_landmarks and self.draw_landmarks == True:
            for hand_landmarks in results.multi_hand_landmarks:
                drawing_utils.draw_landmarks(
                    image,
                    hand_landmarks,
                    hands.HAND_CONNECTIONS,
                    drawing_styles.get_default_hand_landmarks_style(),
                    drawing_styles.get_default_hand_connections_style()
                )

        return results