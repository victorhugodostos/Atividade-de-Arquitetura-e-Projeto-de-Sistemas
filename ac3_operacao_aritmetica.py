#Millene Santos de Oliveira   RA:1900847
#Victor Hugo dos Santos       RA:1901244
def soma(x, y):
    	return x + y

def subtracao(x, y):
	return x - y

def multiplicacao(x, y):
	return x * y

def divisao(x, y):
	return float(x) / y


from ac3_operacao_aritmetica import soma
import unittest
 
class TestSoma(unittest.TestCase):
	def test_soma_inteiros(self):
		self.assertEqual(soma(1,2),3)

	def test_soma_reais(self):
		self.assertEqual(soma(10.5,2),12.5)

	def test_soma_string(self):
		self.assertEqual(soma("abc","def"),"abcdef")

if __name__ == "__main__":
    unittest.main()


class TestSubtracao(unittest.TestCase):
    def test_sub_inteiros(self):
        self.assertEqual(subtracao(1,2),1)
        
    def test_sub_reais(self):       
        self.assertEqual(subtracao(10.5,2),8.5)
    def test_sub_string(self):
        self.assertEqual(subtracao("abcdef","def"),"abc")

if __name__ == "__main__":
    unittest.main()


class TestDivisao(unittest.TestCase):
    def test_div_inteiros(self):
        self.assertEqual(divisao(2,2),1)
        
    def test_div_reais(self):       
        self.assertEqual(divisao(5,2),2.5)

if __name__ == "__main__":
    unittest.main()

class TestMultiplicacao(unittest.TestCase):
    def test_mult_inteiros(self):
        self.assertEqual(multiplicacao(2,2),4)
        
    def test_mult_reais(self):       
        self.assertEqual(multiplicacao(2.5,2),5)

if __name__ == "__main__":
    unittest.main()