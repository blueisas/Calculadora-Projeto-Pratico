def colorcode(cor):
    cores = (
        ('prata', -2),
        ('dourado', -1),
        ('preto', 0),
        ('marrom', 1),
        ('vermelho', 2),
        ('laranja', 3),
        ('amarelo', 4),
        ('verde', 5),
        ('azul', 6),
        ('roxo', 7),
        ('cinza', 8),
        ('branco', 9)
    )

    resistor = 0
    multiplicador = 1

    # cálculo das faixas genéricas
    for cor_nome, cor_valor in cores[2:]:  # percorre a tupla (  ,  ) excluindo a possibilidade de dourado e prata
        if cor_nome in cor:  # quando encontrar na lista a cor inserida pelo usuário, calcula e coontinua procurando
            resistor = (resistor * 10) + cor_valor  # falta pensar na possibilidades de duas faixas da mesma cor e na última faixa sendo cores diferentes de dourado ou prata

    # cálculo da última faixa (multiplicador)
    for cor_nome, cor_valor in cores:
        if cor[-1] == cor_nome:  # verifica a cor da última faixa inserida
            multiplicador = 10 ** cor_valor
            break
            
    resistor *= multiplicador
    return resistor


cores = ['vermelho', 'verde', 'prata']  # teste
print("O valor do resistor é:", colorcode(cores), "ohms")
