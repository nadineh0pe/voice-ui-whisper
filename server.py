from flask import Flask, request, jsonify
import whisper
import tempfile

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio = request.files['audio']

    with tempfile.NamedTemporaryFile(suffix=".webm", delete=True) as tmp:
        audio.save(tmp.name)
        result = model.transcribe(tmp.name)
        return jsonify({'text': result['text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
