import unittest
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_valido(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    