from utils import number_to_binary, cast_binary

def ascii_binary(message):
    final = ''

    for i in message:
        binary = cast_binary(8, number_to_binary(int(ord(i))))
        final += binary

    return final

