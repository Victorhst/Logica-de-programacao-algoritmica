# Ler um número maior que 0 e imprimir a soma de todos os números menores que o número lido.

num = int(input("num: "))
soma = 0

if num > 0:
    for x in range(1, num):
        soma += x

print(soma)
