
def add_padding(input, blocksize):
    if len(input) == blocksize:
        return input
    
    padding = blocksize - len(input) % blocksize
    return input + bytes([padding] * padding)

def has_padding(bin_data):
    padding = bin_data[-bin_data[-1]:]
    
    return all(padding[b] == len(padding) for b in range(0, len(padding)))
 
def remove_padding(data):
    if len(data) == 0 or not has_padding(data):
        return data
    
    padding = data[len(data) - 1]
    return data[:-padding]
               

def main():
    message = b"YELLOW SUBMARINE"
    padded = add_padding(message, 20)

    assert remove_padding(padded) == message


if __name__ == "__main__":
    main()