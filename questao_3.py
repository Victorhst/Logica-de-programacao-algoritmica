# Ler dois números e imprimir todos os números entre eles.
# Suponha que o segundo número é maior que o primeiro.

num1 = int(input("num 1: "))
num2 = int(input("num 2: "))

if num2 > num1:
    for x in range(num1 + 1, num2):
        print(x)
