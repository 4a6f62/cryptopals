import urllib.request

def single_char_xor(input_str, char):
    output = b''
    for byte in input_str:
        output += bytes([byte ^ char])
    return output

def get_english_score(input_bytes):
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])    

url = 'https://cryptopals.com/static/challenge-data/4.txt'
response = urllib.request.urlopen(url)
data = response.read()
output = data.decode('utf-8')
lines_in_file = output.split("\n")

best_scores = []
for hexstring in lines_in_file:
    potential_messages = []
    ciphertext = bytes.fromhex(hexstring)
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
  
    best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print("{}: {}".format(item.title(), best_score[item]))
    
    best_scores.append(best_score)

bestest_score = sorted(best_scores, key=lambda x: x['score'], reverse=True)[0]

print('--------------------------------------------------------------------')
for item in bestest_score:
    print("{}: {}".format(item.title(), bestest_score[item]))
