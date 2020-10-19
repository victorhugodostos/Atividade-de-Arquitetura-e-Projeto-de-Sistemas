#Millene Santos de Oliveira   RA:1900847
#Victor Hugo dos Santos       RA:1901244
import pytest
import math

print("EQUACAO DE SEGUNDO GRAU")
print("ax^2 + bx + c = 0")

a = float(input("Digite a variável a: "))
b = float(input("Digite a variável b: "))
c = float(input("Digite a variável c: "))

#calcular discriminante - delta
delta = (b**2) - (4*a*c)
#print("delta é", delta)
#calcular as raizes
if (delta < 0):
    print("esta equação não possui raízes reais")
else:
    if (delta == 0):
        x = (-b) / (2*a)
        print("a raiz desta equação é", x)
    else:
        x_pos = ((-b) + math.sqrt(delta)) / (2*a)
        x_neg = ((-b) - math.sqrt(delta)) / (2*a)
        if (x_pos <= x_neg):
            print("as raízes da equação são", x_pos, "e", x_neg)
        else:
            print("as raízes da equação são", x_neg, "e", x_pos)

@pytest.mark.parametrize("valor_a, valor_b, valor_c, resposta_1, resposta_2",[(-1,2,0,-0.0,2.0), (8, 4, 1, -0.5, -0.25)])

def test_bhaskara(valor_a, valor_b, valor_c, resposta_1, resposta_2):
	assert b.calcula_bhaskara(valor_a, valor_b, valor_c) == (resposta_1, resposta_2)
