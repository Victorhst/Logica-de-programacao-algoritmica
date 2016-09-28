# João tem 1,50 metros e cresce 2 centímetros por ano, enquanto
# Maria tem 1,10 metros e cresce tem 3 centímetros por ano. Construa um
# algoritmo (pseudocódigo e fluxograma) que calcule e imprima quantos anos
# serão necessários para que Maria seja maior que João.

alt_joao = 1.50
alt_maria = 1.10

cresc_joao = 0.02
cresc_maria = 0.03

cont_anos = 0

while alt_maria < alt_joao:
    alt_joao += cresc_joao
    alt_maria += cresc_maria
    cont_anos += 1

print(cont_anos)
print(alt_joao)
print(alt_maria)
