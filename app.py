from flask import Flask, request, jsonify
from model import generator

app = Flask(__name__)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.get_json()

    if 'input_text' not in data:
        return jsonify({'error': 'No input text provided'}), 400

    input_text = data['input_text']

    # Generate a response
    response = generator(input_text, max_length=50)
    generated_text = response[0]['generated_text']

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)