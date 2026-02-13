BASE64_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def number_to_binary(number):

    """
    Esta función convierte un número decimal a número binario
    Args:
        number (int): el número decimal que queremos convertir a binario
    
    Returns:
        binary: el número en formato binario
    """
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    
    return number_to_binary(int(number/2)) + str(number % 2)


def cast_binary(base, bin_number):

    """
    Esta función toma un número binario y le agrega los 0's necesarios para que el número sea representado en una base en específica
    Args:
        bin_number (str): Cadena binaria a castear (ej: '0110')
        base (int): La base a la cuál queremos castear el número (ej: base 8).
    
    Returns:
        bin: el número binario casteado (00000110)
    """
    if len(bin_number) < base:
        return bin_number.zfill(base)
    
    return bin_number

def binary_string_to_decimal(binary):
 
    """
    Esta función toma un número en notación binaria y lo convierte a notación decimal
    Args:
        binary (str): El número binario que queremos convertir (ej: '0110')
    
    Returns:
        decimal: el número decimal resultante de la operación
    """
    decimal = 0
    for i in range(len(binary)):
        if binary[::-1][i] == '1':
            decimal += (2**i)
    return decimal


def divide_binary_string(binary, division):
    """
    Divide una cadena binaria en fragmentos de tamaño especificado.
    
    Esta función toma una cadena binaria y la divide en fragmentos de tamaño 'division'.
    Si el último fragmento es más corto que el tamaño especificado, se rellena con ceros
    a la derecha para alcanzar el tamaño requerido.
    
    Args:
        binary (str): Cadena binaria a dividir (ej: '11010110').
        division (int): Tamaño de cada fragmento en el que dividir la cadena.
    
    Returns:
        list: Lista de cadenas binarias, donde cada elemento es un fragmento de tamaño 'division'.
              El último fragmento se rellena con ceros si es necesario.
    """
    divided = []
    for i in range(0, len(binary), division):
        divided.append(binary[i:i+division].ljust(division, '0'))
    return divided
