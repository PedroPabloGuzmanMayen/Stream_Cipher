import random
import string
from xor import binary_xor
from binario_ascci import ascii_binary
from binary_ascii import binary_to_ascii

def generate_key(size, seed):
    """
    Genera una llave para cifrar mensajes, utliza random para generar una cadena ascii al azar
    
    Args:
        size (int): El tamaño de la llave que vamos a generar

    Returns:
        key: la llave generada
    """
    random.seed(seed)
    char_string = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(char_string) for _ in range(size))
    return key

def stream_cipher(message, seed):
    """
    Genera una llave con la función anterior del mismo tamaño que el mensaje, convierte el mensaje y la llave a binary, aplica xor y el
    resultado lo convierte a ascii
    
    Args:
        message(str): el mensaje a cifrar

    Returns:
        final: el mensaje en ascii luego de aplicar xor
    """
    key = generate_key(len(message), seed)
    print(f'LLave:{key} ')
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    bin_xor = binary_xor(bin_message, bin_key)

    return binary_to_ascii(bin_xor)

print(generate_key(10, 4))
print(generate_key(10, 3))
print(generate_key(10, 80))