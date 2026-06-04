from flask import Flask, render_template, request, jsonify
from jwt_audit import analyze_token_web

app = Flask(__name__)

@app.route('/')
def index():
    # Frontend tasarımımızı ekrana basar
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Web sitesinden gelen token'ı alır, analiz eder ve sonucu geri yollar
    data = request.json
    token = data.get('token')
    result = analyze_token_web(token, 'wordlist.txt')
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)