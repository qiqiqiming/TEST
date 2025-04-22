from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 'Hello World!',
        'status': 'success'
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route("/")
def home():
    return jsonify({"message": "Hello from Railway + Flask!"})
if __name__ == '__main__':
    app.run(debug=True) 