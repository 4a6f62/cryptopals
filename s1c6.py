import binascii
import urllib.request
import base64

from s1c5 import repeating_xor_key
from s1c3 import get_potential_message

def ham_distance(str1, str2):      
    distance = 0
    for ch1, ch2 in zip(bytes_to_binary(str1), bytes_to_binary(str2)):
            if ch1 != ch2:
                    distance += 1
    return distance

def bytes_to_binary(bytes_code):
    result = ""
    for i in range(len(bytes_code)):
        new_bin = str(bin(bytes_code[i]))[2:]
        while len(new_bin) < 8:
            new_bin = "0" + new_bin
        result += new_bin
    return result

def break_string(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]

def avg_ham_distance(bytes_code, keysize):
    chunks = break_string(bytes_code, keysize)
    total_distance = 0
    for i in range(len(chunks)-1):
        total_distance += ham_distance(chunks[i], chunks[i + 1])
    return total_distance / len(chunks) / keysize

def find_keysizes(ciphertext):
    distances = []

    for keysize in range(2, 41):
        distances.append(avg_ham_distance(ciphertext, keysize))

    best_keys = []
    for i in range(3):
        min_distance = min(distances)
        min_distance_key = distances.index(min_distance)
        best_keys.append(min_distance_key+2)
        distances[min_distance_key] = 100

    return best_keys

def make_transposed_blocks(bytes_code, keysize):
    transposed_blocks = [b""] * keysize
    i = 0
    j = 0
    while i < len(bytes_code):
        transposed_blocks[j] += bytes([bytes_code[i]])
        i += 1
        if (j < keysize - 1):
            j += 1
        else:
            j = 0
    return transposed_blocks

def main():
    b64_codes = open('s1c6.txt', 'r')
    ciphertext = b""
    for line in b64_codes:
        ciphertext += base64.b64decode(line[0:-1])
      
    keysizes = find_keysizes(ciphertext)
    messages = []
    best_keys = {}
    for keysize in keysizes:
        best_of_size = b""
        total_score = 0
        transposed_blocks = make_transposed_blocks(ciphertext, keysize)
        for transposed_block in transposed_blocks:
            message = get_potential_message(transposed_block)
            total_score += message['score']
            best_of_size += bytes([message['key']])
            messages.append(message)
        best_keys[total_score/keysize] = best_of_size
    
    best_score = max(best_keys.keys())
    key = best_keys[best_score]
    print(key)

    decoder_bytes = key * (len(ciphertext)//len(key)) + key
    decoder_bytes = decoder_bytes[:len(ciphertext)]
    print(repeating_xor_key(ciphertext,decoder_bytes))

if __name__ == '__main__':
    main()