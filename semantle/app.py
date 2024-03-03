from flask import Flask, jsonify, request
from deploy import find_similar_words
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/getpossiblevalues', methods=['POST'])
def getpossiblevalues():
    data = request.get_json()
    # guess = request.args.get('guess', '') 
    # score = float(request.args.get('score', 0))
    # possible_words = request.args.get('possible', [])

    # if guess score or possible_words are not in the request body, return bad request
    if data is None or 'guess' not in data or 'score' not in data or 'possible' not in data:
        missing_params = [param for param in ["guess", "score", "possible"] if param not in data]
        return jsonify({"error": f"Missing required parameters: {', '.join(missing_params)}"}), 400

    guess = data['guess'] 
    score = data['score']
    possible_words = data['possible']
    
    try:
        score = float(score)
    except ValueError:
        return jsonify({"error": "score must be a number"}), 400

    if possible_words == []:
        result = list(find_similar_words(guess, score).keys())
    else:
        result = list(find_similar_words(guess, score, possible_words).keys())


    return jsonify({"possible": result})

app.run(debug=True, port=8080, host="0.0.0.0")