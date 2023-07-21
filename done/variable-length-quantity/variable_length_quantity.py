def get_encoded_number(number):
    result = []
    bin_str_rev = ''.join(reversed(bin(number)[2:]))
    for start in range(0, len(bin_str_rev), 7):
        end = start + 7 if start + 7 <= len(bin_str_rev) else len(bin_str_rev)
        byte = int(''.join(reversed(bin_str_rev[start:end])),2)
        byte = byte + 0x80 if start else byte
        result.insert(0, byte)
    return result

def encode(numbers: list):
    result = []
    for number in numbers:
        encoded_number = get_encoded_number(number)
        for element in encoded_number:
            result.append(element)
    return result


def decode(bytes_: list):
    result = []
    bin_str = ""
    while bytes_:
        byte = bytes_.pop(0)
        byte_str = bin(byte)[2:]
        if byte < 0x80:
            byte_str = '0' * (7 - len(byte_str)) + byte_str
            bin_str += byte_str
            result.append(int(bin_str,2))
            bin_str = ""
        else:
            bin_str += byte_str[1:]
    
    if not result:
        raise ValueError("Bad Format")
    
    return result
    

    

if __name__ == "__main__":
    print(decode([0xC0, 0x0]))