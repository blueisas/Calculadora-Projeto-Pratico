from itertools import product


def tabela_verdade(vin):  # todas as combinações possíveis de 0 e 1 len(variables) vezes
    tabela = list(product([0, 1], repeat=len(vin)))
    return tabela


def mapa_karnaugh(vin, func):
    tabela = tabela_verdade(vin)
    t = [[func(*binario) for binario in linha] for linha in tabela]


vin = ['a', 'b']
func = lambda a, b: a and not b

print(tabela_verdade(vin))
