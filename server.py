"""This module contains a Flask application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector1():
    """Analyze text to detect the dominant emotion."""
    text_to_analyse = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyse)
    
    if resp['dominant_emotion'] is None:
        return "<b> Invalid text! Please try again!<b>"
    
    formatted_output = (f"For the given statement, the system response is "
                        f"'anger': {resp['anger']}, 'disgust': {resp['disgust']}, "
                        f"'fear': {resp['fear']}, 'joy': {resp['joy']} and "
                        f"'sadness': {resp['sadness']}. "
                        f"The dominant emotion is <u><b>{resp['dominant_emotion']}</b></u>.")
    return formatted_output

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
