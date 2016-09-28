# Faça um algoritmo (pseudocódigo e fluxograma) que lê o nome de um
# produto, o preço e a quantidade comprada. Escreva o nome do produto comprado e o
# valor total a ser pago, considerando que são oferecidos descontos pelo número de
# unidades compradas, segundo a tabela abaixo:
#
#
#  a) Até 10 unidades: valor total
#  b) De 11 a 20 unidades: 10% de desconto
#  c) De 21 a 50 unidades: 20% de desconto
#  d) Acima de 50 unidades: 25% de desconto

prdt = str(input("Nome do produto: "))
preco = float(input("Preço indicado na embalagem: "))
qtd = int(input("Quantidade comprada: "))


if qtd < 10:
    result = preco * qtd
    print("Não há desconto para compras abaixo de 10 unidades.")

elif qtd in range(11, 20):
    result = ((10/100) * preco) * qtd
    print("Desconto de 10% para compras entre 11 e 20 unidades.")

elif qtd in range(21, 50):
    result = ((20/100) * preco) * qtd
    print("Desconto de 20% para compras entre 21 e 50 unidades.")

else:
    result = ((25/100) * preco) * qtd
    print("Desconto de 25% para compras acima de 50 unidades.")

print("O produto esolhido foi {}. Valor total a ser pago (incluindo descontos): R${}".format(prdt, result))
