def sxor(str1, str2):
    output = b''
    for i in range(len(str1)):
        output += bytes([str1[i] ^ str2[i]])
    return output


str1 = input("String 1: ")
str2 = input("String 2: ")

bytes1 = bytes.fromhex(str1)
bytes2 = bytes.fromhex(str2)

print(str1)
print(str2)
result = sxor(bytes1, bytes2)
hex_str = result.hex()

print(result)
print(hex_str)
