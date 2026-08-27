frase = "Eu estudo linguagem de programação por amar a cadeira"
frase_lista = frase.split()
frase_lista_4letras = []

for x in frase_lista:
    if len(x) > 4:
        frase_lista_4letras.append(x)

print(f"Lista com 4 palavras formada: {frase_lista_4letras}")
# QUESTÃO 10
#
# Crie uma frase contendo várias palavras.
#
# Depois:
#
# 1. Transforme a frase em uma lista usando split();
#
# 2. Crie uma segunda lista vazia para armazenar
#    as palavras que possuem mais de 4 caracteres;
#
# 3. Percorra a lista de palavras utilizando for;
#
# 4. Verifique quais palavras possuem mais de
#    4 caracteres utilizando len();
#
# 5. Adicione essas palavras à segunda lista
#    utilizando append();
#
# 6. Mostre a segunda lista;
#
# 7. Mostre quantas palavras foram encontradas
#    utilizando len().
#
# Não utilize recursos que ainda não foram ensinados.