from flask import Flask, render_template, request


app = Flask(__name__)

alphabet = str('abcdefghijklmnopqrstuvwxyz')
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
numbers = '0123456789'


@app.route('/result', methods=['POST'])
def code_maker():
    res = ''
    key_code = int(request.form['key_code'])
    text = request.form['text']
    for code in text:
        if code in alphabet:
            res += alphabet[(alphabet.index(code) + key_code) % len(alphabet)]
        elif code == ' ':
            res += ' '
        elif code in punctuation:
            res += punctuation[(punctuation.index(code) + key_code) % len(punctuation)]
        elif code in numbers:
            res += numbers[(numbers.index(code) + key_code) % len(numbers)]
        else:
            continue
    return render_template('result_second.html', res=res)


@app.route('/', methods=['GET'])
def hello():
    return render_template('hello_second.html')


if __name__ == '__main__':
    app.run()
