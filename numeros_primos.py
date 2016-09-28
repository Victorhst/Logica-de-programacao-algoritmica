N = 47

if N % 2 != 0 \
        and N % 3 != 0 \
        and N % 5 != 0 \
        and N % 7 != 0:
    result = 'É primo.'

else:
    result = 'Não é primo.'

print(result)
