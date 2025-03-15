from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)
    if not result["dominant_emotion"]:
        return "Invalid text! Please try again!"
    anger, disgust, fear, joy, sadness, dominant = result["anger"], result["disgust"], result["fear"], result["joy"], result["sadness"], result["dominant_emotion"]
    formatted = "For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."
    return formatted.format(anger=anger, disgust=disgust, fear=fear, joy=joy, sadness=sadness, dominant=dominant)

if __name__ == '__main__':
    app.run()