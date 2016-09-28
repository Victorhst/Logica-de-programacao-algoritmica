valor = 1

while valor <= 100:
    aux = 1
    contador = 0

    while aux <= valor:
        if valor % aux == 0:
            contador += 1

        aux += 1

    if contador == 2:
        print(valor)

    valor += 1
