num = int(input("Digite um número entre 0 e 100: "))

while num <= 100:
    if num % 2 != 0 \
            and num % 3 != 0 \
            and num % 5 != 0 \
            and num % 7 != 0:
        print(num, "é número primo;")
    num += 1
