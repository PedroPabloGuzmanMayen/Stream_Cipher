import random
import string
from xor import binary_xor
from binario_ascci import ascii_binary
from binary_ascii import binary_to_ascii

def generate_keystream(size, seed):
    '''
    Genera una llave para cifrar mensajes, utliza random para generar una cadena ascii al azar
    
    Args:
        size (int): El tamaño de la llave que vamos a generar
        seed (str): La semilla para el algoritmo pseudoaleatorio

    Returns:
        key: la llave generada
    '''
    random.seed(seed)
    char_string = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(char_string) for _ in range(size))
    return key

def stream_cipher(message, key):
    '''
    Genera una llave con la función anterior del mismo tamaño que el mensaje, convierte el mensaje y la llave a binary, aplica xor y el
    resultado lo convierte a ascii
    
    Args:
        message(str): el mensaje a cifrar
        key(str): la llave que vamos a usuar para generar el key_stream

    Returns:
        final: el mensaje en ascii luego de aplicar xor
    '''
    
    key_stream = generate_keystream(len(message), key)
    print(f'LLave:{key_stream} ')
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key_stream)
    bin_xor = binary_xor(bin_message, bin_key)

    return binary_to_ascii(bin_xor)


def main():
    print('=== STREAM CIPHER CON PRNG ===')

    while True:
        print('\n--- Nueva prueba ---')
        key = input('Clave (seed): ')
        msg = input('Mensaje: ')

        cipher = stream_cipher(msg, key)
        print('\nTexto cifrado (hex):', cipher.encode('latin-1').hex())

        decrypted = stream_cipher(cipher, key)
        print('Texto descifrado:', decrypted)

        again = input('\n¿Otra prueba? (s/n): ')
        if again.lower() != 's':
            break


if __name__ == '__main__':
    main()