from flask import Flask, render_template, request
from string import ascii_lowercase


app = Flask(__name__)


@app.route('/result', methods=['POST'])
def counter():
    word = request.form['word']
    alphabet = {k: 0 for k in ascii_lowercase}
    for letter in word:
        if not alphabet[letter]:
            alphabet[letter] += 1
    return render_template('result.html', alphabet=alphabet)


@app.route('/', methods=['GET'])
def hello():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
