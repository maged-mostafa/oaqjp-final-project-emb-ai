import requests
import json

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
    "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse):
    """
    Analyze the emotions in the supplied text using
    the Watson NLP Emotion Prediction API.
    """

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=input_json
    )

    return response.json()["emotionPredictions"][0]["emotion"]