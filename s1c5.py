def repeating_xor_key(input_str, key):
    output = b''
    index = 0
    for byte in input_str:
        output += bytes([byte ^ key[index]])
        index += 1
        if(index >= len(key)):
            index = 0
    return output

def main():
    str1 = str.encode(input('String to encrypt: '))
    key = str.encode(input('Key to encrypt with: '))

    output = repeating_xor_key(str1, key)
    print(output.hex())


if __name__ == '__main__':
    main()