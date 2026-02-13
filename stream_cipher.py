import random
import string
from xor import binary_xor
from binario_ascci import ascii_binary
from binary_ascii import binary_to_ascii

def generate_keystream(size, seed):
    """
    Genera una llave para cifrar mensajes, utliza random para generar una cadena ascii al azar
    
    Args:
        size (int): El tamaño de la llave que vamos a generar
        seed (int): La semilla para el algoritmo pseudoaleatorio

    Returns:
        key: la llave generada
    """
    random.seed(seed)
    char_string = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(char_string) for _ in range(size))
    return key

def stream_cipher(message, key):
    """
    Genera una llave con la función anterior del mismo tamaño que el mensaje, convierte el mensaje y la llave a binary, aplica xor y el
    resultado lo convierte a ascii
    
    Args:
        message(str): el mensaje a cifrar

    Returns:
        final: el mensaje en ascii luego de aplicar xor
    """
    print(f'LLave:{key} ')
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    bin_xor = binary_xor(bin_message, bin_key)

    return binary_to_ascii(bin_xor)

def main():
    print('=== STREAM CIPHER CON PRNG ===\n')

    seed = int(input('Ingrese la seed (clave numérica): '))
    size = int(input('Ingrese el tamaño del keystream: '))

    keystream = generate_keystream(size, seed)
    print(f'\nLa llave generada es: {keystream}')
    print('Guárdela, es necesaria para cifrar y descifrar\n')

    message = input('Ingrese el mensaje a cifrar: ')

    if len(message) > len(keystream):
        print('Error: la llave debe ser al menos del tamaño del mensaje')
        return

    key_used = keystream[:len(message)]

    print('\n--- CIFRADO ---')
    ciphertext = stream_cipher(message, key_used)
    print(f'Texto cifrado: {ciphertext}')

    print('\n--- DESCIFRADO ---')
    key_input = input('Ingrese la misma llave para descifrar: ')

    if len(key_input) != len(ciphertext):
        print('Error: la llave ingresada no tiene el tamaño correcto')
        return

    plaintext = stream_cipher(ciphertext, key_input)
    print(f'Texto original: {plaintext}')


if __name__ == '__main__':
    main()
