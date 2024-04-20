def colorcode(cor):
    cor = (
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
        while cor_nome in cor[:-1]:  # percorre todas as faixas encontrando a cor, exceto a última
            resistor = (resistor * 10) + cor_valor  # calcula
            cor.remove(cor_nome)  # remove a cor da lista das faixas

    # cálculo da última faixa (multiplicador)
    for cor_nome, cor_valor in cores:
        if cor[-1] == cor_nome:  # testa a cor da última faixa do resistor
            multiplicador = 10 ** cor_valor  # calcula quando encontra
            break  # quebra o loop (não precisa encontrar mais nada)
    resistor *= multiplicador  # adiciona a última faixa ao valor do resistor
    return resistor


cores = ['vermelho', 'vermelho','vermelho', 'prata']  # teste
print("O valor do resistor é:", colorcode(cores), "ohms")
