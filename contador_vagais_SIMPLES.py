texto = str(input("Digite seu texto: "))

if texto.isalnum():
    print('Texto alfanumérico.')

print("""Contém {} vogais 'a', {} vogais 'e', {} vogais 'i', {} vogais 'o' \
e {} vogais 'u'.""".format(texto.count('a'), texto.count('e'), texto.count('i'), texto.count('o'), texto.count('u')))
