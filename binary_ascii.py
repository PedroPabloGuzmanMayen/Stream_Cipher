from utils import divide_binary_string, binary_string_to_decimal

def binary_to_ascii(binary):
    if len(binary) % 8 != 0:
        characters = divide_binary_string(binary[:-(len(binary) % 8)],8)
    else:
        characters = divide_binary_string(binary,8)
    final = ''
    for i in characters:
        final += chr(binary_string_to_decimal(i))

    return final



