# Lei de ohm
def tensao(r, i):
    v = r * i
    return v


def resistencia(v, i):
    r = v / i
    return r


def corrente(v, r):
    i = v / r
    return i


# Potência
def potencia(v, i):
    p = v * i
    return p


# Componentes
def resistor(vin, vr2, i):
    r1 = abs(vin - vr2) / i
    return r1


def vout(r2, r1, vin):
    v_out = r2 / (r1 + r2) * vin
    return v_out


n1 = float(input('Insira o valor 1: '))
n2 = float(input('Insira o valor 2: '))
n3 = float(input('Insira o valor 3: '))

# print(tensao(n1, n2))
# print(resistencia(n1, n2))
# print(corrente(n1, n2))
# print(potencia(n1, n2))
# print(resistor(n1, n2, n3))
# print(vout(n1, n2, n3))

