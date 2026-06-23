import os
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
    # Render автоматически передает порт в переменные окружения PORT.
    # Если мы запускаем локально, сработает дефолтное значение 5000.
    port = int(os.environ.get("PORT", 5000))
    
    # На Render крайне важно слушать хост 0.0.0.0, чтобы сервер принимал внешние запросы
    app.run(host='0.0.0.0', port=port, debug=False)