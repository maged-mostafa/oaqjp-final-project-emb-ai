import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion detector.
    """

    def test_emotion_detector(self):
        """
        Test dominant emotions for different sentences.
        """
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }

        for text, expected in test_cases.items():
            response = emotion_detector(text)
            self.assertEqual(
                response["dominant_emotion"],
                expected
            )


if __name__ == "__main__":
    unittest.main()