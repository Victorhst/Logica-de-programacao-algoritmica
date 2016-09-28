# Ler um número maior que zero e imprimir o quadrado de todos os números entre 0 e o número lido.

num = int(input("num: "))

if num > 0:
    for x in range(1, num):
            print(x**2)
