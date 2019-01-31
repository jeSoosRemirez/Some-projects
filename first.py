from flask import Flask, jsonify
from string import ascii_lowercase


app = Flask(__name__)


@app.route('/<string:word>', methods=['GET'])
def counter(word):
    alphabet = {k: 0 for k in ascii_lowercase}
    for letter in word:
        if not alphabet[letter]:
            alphabet[letter] += 1
    return jsonify(alphabet)


if __name__ == '__main__':
    app.run(debug=True)
