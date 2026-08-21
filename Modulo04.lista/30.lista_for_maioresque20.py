lista = [2,4,50,32,20,21,22,24,19,1]
lista2 = []
quantidade = 0
for numero in lista:
    if numero > 20:
        quantidade = quantidade + 1
        lista2.append(numero)


print(f"Numeros encontrados maiores que 20:{quantidade}")
print(f"Os numeros são:{lista2}")

# QUESTÃO 30
#
# Crie uma lista contendo 10 números inteiros.
#
# Utilize um for para percorrer a lista.
#
# O programa deve:
#
# 1. Mostrar somente os números maiores que 20;
# 2. Contar quantos números maiores que 20 existem na lista;
# 3. Ao final, mostrar a quantidade encontrada.
#
# Não utilize range() nem índices.
#
# Exemplo:
#
# Lista: [10, 25, 8, 30, 15, 40, 12, 22, 5, 50]
#
# Números maiores que 20:
# 25
# 30
# 40
# 22
# 50
#
# Quantidade de números maiores que 20: 5