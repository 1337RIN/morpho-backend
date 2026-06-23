from flask import Flask, request, jsonify
from flask_cors import CORS # Импортируем CORS
from main import analyze_sentence

app = Flask(__name__)
CORS(app) # Разрешаем перекрестные запросы для всего приложения

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Передайте текст в поле 'text'"}), 400
    text = data['text']
    analysis_result = analyze_sentence(text)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)