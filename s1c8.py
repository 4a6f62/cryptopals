import binascii

def Is_ECB(ciphertext):
    chunks = [ciphertext[i*16:(i+1)*16] for i in range(int(len(ciphertext)/16))]

    duplicates = len(chunks) - len(set(chunks))


    if(duplicates >= 1):
        return True, duplicates
    else:
        return False, 0
    
def main():
    highest_duplicates = 0
    line_counter = 0
    AES_Cipher = b""

    with open('8.txt') as fin:
        for line in fin:

            line_counter += 1
            ECB, duplicates = Is_ECB(line)

            if(ECB):
                AES_cipher = line
                highest_duplicates = duplicates
                line_number = line_counter
                break

    print("Cipher: {}\nNumber: {}\nLine:{}".format(AES_cipher, highest_duplicates, line_number))
    
    
if __name__ == '__main__':
    main()