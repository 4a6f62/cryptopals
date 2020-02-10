import base64

hexstring = input("String 1: ")
message_bytes = bytes.fromhex(hexstring)
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(message_bytes)
print(base64_bytes)
print(base64_message)
