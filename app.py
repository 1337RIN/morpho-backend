import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from main import analyze_sentence

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Передайте текст в поле 'text'"}), 400
    text = data['text']
    analysis_result = analyze_sentence(text)
    return jsonify(analysis_result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    
    app.run(host='0.0.0.0', port=port, debug=False)
