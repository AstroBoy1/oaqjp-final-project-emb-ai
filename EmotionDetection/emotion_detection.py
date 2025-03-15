import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=input_json)
    status_code = response.status_code
    if status_code == 400:
        return {'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None}
    text = response.json()
    anger_score = text["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = text["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = text["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = text["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = text["emotionPredictions"][0]["emotion"]["sadness"]
    scores = {'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score}
    dominant = max(scores, key=scores.get)
    scores["dominant_emotion"] = dominant
    return scores

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))