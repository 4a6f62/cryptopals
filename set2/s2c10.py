from Crypto.Cipher import AES
from s2c09 import add_padding, remove_padding
from base64 import b64decode, b64encode

def encrypt_ecb(data, key, block_size):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = add_padding(data, block_size)
    return cipher.encrypt(padded)

def decrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = cipher.decrypt(data)
    return remove_padding(padded)

def sxor(str1, str2):
    return bytes([b1 ^ b2 for b1, b2 in zip(str1, str2)])

def encrypt_cbc(ciphertext, key, iv, block_size):
    result = b''
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    for block in blocks:
        block_cipher_input = sxor(block, iv)            
        encrypted_block = encrypt_ecb(block_cipher_input, key, block_size)
        iv = encrypted_block        
        result += encrypted_block
    
    return result

def decrypt_cbc(ciphertext, key, iv, block_size):
    result = b''
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    for block in blocks:
        decrypted_block = decrypt_ecb(block, key)        
        plaintext = sxor(iv, decrypted_block)        
        iv = block        
        result += plaintext
    
    return result

def main():
    key = b"YELLOW SUBMARINE"
    iv = b'\x00' * AES.block_size
        
    with open("10.txt") as input_file:
        data = b64decode(input_file.read())  
    input_file.close()
    
    plaintext = decrypt_cbc(data, key, iv, AES.block_size)
    encrypted = encrypt_cbc(plaintext, key, iv, AES.block_size)
    string = str(b64encode(encrypted),'utf-8')
    
    with open("10out.txt", "w") as output_file:
        output_file.write('\n'.join(string[i:i+60] for i in range(0, len(string), 60)))
    output_file.close()
    
    print(plaintext)    
        
if __name__ == "__main__":
    main()