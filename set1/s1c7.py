from Crypto.Cipher import AES
import base64

def decrypt_ecb_with_cipher(ciphertext, cipher):
    cipher = AES.new(cipher.encode("utf8"), AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def main():
    key = 'YELLOW SUBMARINE'
        
    with open('s1c7.txt') as fh:
        ciphertext = base64.b64decode(fh.read())
    
    print(decrypt_ecb_with_cipher(ciphertext, key))

if __name__ == '__main__':
    main()
    