def binary_xor(binary1, binary2):
    """
    Aplica XOR para 2 cadenas binarias, si no tienen el mismo tamaño entonces tira un error
    
    Args:
        binary1(str): La cadena binaria a la que se le aplciara XOR.
        binary2(str): La cadena binaria que se usará para aplicar XOR.

    Returns:
        mensaje final: la cadena resultante luego de aplicar XOR
    """
    if len(binary1) != len(binary2):
        raise ValueError('Las cadenas deben tener la misma longitud')

    final = ''
    for b1, b2 in zip(binary1, binary2):
        final += '1' if b1 != b2 else '0'

    return final
