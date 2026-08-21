# QUESTÃO 25
#
# Crie uma lista vazia chamada "numeros".
#
# Utilize um comando for para percorrer os números de 1 até 5.
#
# A cada repetição, adicione o número atual à lista
# utilizando append().
#
# Ao final:
#
# 1. Mostre a lista completa;
# 2. Mostre a quantidade de elementos utilizando len().
#
# Resultado esperado:
#
# Lista: [1, 2, 3, 4, 5]
# Quantidade de elementos: 5

numeros = []

for cont in range(1, 6):
    numeros.append(cont)
print("-----------------------------------------------")
print(f"Lista completa:{numeros}")
print(f"Quantidade de numeros na lista:{len(numeros)}")
print("-----------------------------------------------")