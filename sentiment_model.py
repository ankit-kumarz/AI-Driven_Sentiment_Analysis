from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get("text", "")
    
    if not text:  
        return jsonify({"error": "Text is required!"}), 400
    
    sentiment_score = TextBlob(text).sentiment.polarity

    if sentiment_score > 0:
        result = "Positive 😊"
    elif sentiment_score < 0:
        result = "Negative 😞"
    else:
        result = "Neutral 😐"

    return jsonify({"sentiment": result, "score": sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)
