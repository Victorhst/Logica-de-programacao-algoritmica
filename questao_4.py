# Leia o algoritmo abaixo, que realiza a soma de todos os números inteiros até "num", indique o erro e corrija-o:

num = int(input("num: "))
contador = 0
soma = 0

while contador < num:
    soma += contador
    contador += 1

print(soma)


# O "print" deve imprimir a soma, e não o contador.
