import unittest
from stream_cipher import stream_cipher


class TestStreamCipher(unittest.TestCase):

    def test_decrypt_recovers_plaintext(self):
        msg = 'Hola mundo'
        key = 'clave123'
        cipher = stream_cipher(msg, key)
        plain = stream_cipher(cipher, key)
        self.assertEqual(plain, msg)

    def test_different_keys_produce_different_ciphertext(self):
        msg = 'Mensaje secreto'
        c1 = stream_cipher(msg, 'clave1')
        c2 = stream_cipher(msg, 'clave2')
        self.assertNotEqual(c1, c2)

    def test_same_key_is_deterministic(self):
        msg = 'Probando determinismo'
        key = 'misma_clave'
        c1 = stream_cipher(msg, key)
        c2 = stream_cipher(msg, key)
        self.assertEqual(c1, c2)

    def test_different_lengths(self):
        key = 'clave'
        messages = [
            'A',
            'Hola',
            'Esto es un mensaje más largo de prueba',
            ''
        ]

        for msg in messages:
            cipher = stream_cipher(msg, key)
            plain = stream_cipher(cipher, key)
            self.assertEqual(plain, msg)


if __name__ == '__main__':
    unittest.main()
