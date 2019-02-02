alphabet = str('abcdefghijklmnopqrstuvwxyz')
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
numbers = '0123456789'
res = ''

key_code = int(input('Type key: '))
text = input('Type text: ').lower()

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

print(res)
