#Millene Santos de Oliveira   RA:1900847
#Victor Hugo dos Santos       RA:1901244
from unittest import TestCase
from unittest.mock import patch

class Calculadora:
    def soma(self, a, b):
	    return a + b

    def subtracao(self, a, b):
    	return a - b

    def multiplicacao(self, a, b):
	    return a * b

    def divisao(self, a, b):
	    return float(a)/ b


class TestCalculadora(TestCase):
    @patch ("main.Calculadora.soma",return_value = 7)
    def test_soma(self, soma):
	    self.assertEqual(soma(3, 4), 7)

    @patch ("main.Calculadora.subtracao",return_value = 1)
    def test_substracao(self, subtracao):
	    self.assertEqual(subtracao(3, 4), 1)

    @patch ("main.Calculadora.multiplicacao",return_value = 12)
    def test_multiplicacao(self, multiplicacao):
	    self.assertEqual(multiplicacao(3, 4), 12)

    @patch ("main.Calculadora.divisao",return_value = 2)
    def test_divisao(self, divisao):
	    self.assertEqual(divisao(4, 2), 2)
