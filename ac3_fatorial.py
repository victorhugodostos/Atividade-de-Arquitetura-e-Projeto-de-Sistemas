#Millene Santos de Oliveira   RA:1900847
#Victor Hugo dos Santos       RA:1901244
import pytest

def fatorial():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! eh =" %n, fat)
fatorial()

@pytest.mark.parametrize("N1, N2",[(0,1),(1,1),(2,2),(3,6),(4,24),(5,120),])

def teste_fatorial(N1,N2):
    assert fatorial(N1) == N2