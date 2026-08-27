frase = "   Eu amo comer açai dia de domingo   "
print("------------------------------------------")
print(f"Frase original:{frase}")
print("------------------------------------------")
print(f"Frase sem os espaços, usando strip:{frase.strip()}")
print("------------------------------------------")
print(f"Frase transformada em lista, usando split:{frase.split()}")
print("------------------------------------------")
print(f"Quantidade de palavras que possuem na lista:{len(frase.split())}")
print("------------------------------------------")
# QUESTÃO 11
#
# Crie uma frase contendo espaços extras
# no começo e no final.
#
# Depois:
#
# 1. Mostre a frase original;
#
# 2. Remova os espaços do começo e do final
#    utilizando strip();
#
# 3. Transforme a frase limpa em uma lista
#    de palavras utilizando split();
#
# 4. Mostre a lista de palavras criada;
#
# 5. Mostre quantas palavras existem nessa lista
#    utilizando len().
#
# Atenção:
# A quantidade solicitada no item 5 é a quantidade
# de PALAVRAS da lista criada pelo split(),
# e não a quantidade de caracteres da frase.