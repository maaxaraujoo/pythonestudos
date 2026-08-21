# QUESTÃO 23
#
# Crie uma lista contendo 8 números inteiros.
#
# Depois:
#
# 1. Mostre a lista completa;
# 2. Mostre a quantidade de elementos utilizando len();
# 3. Mostre o primeiro elemento;
# 4. Mostre o último elemento.
#
# ATENÇÃO:
# Não informe diretamente o índice do último elemento.
# Utilize len() para descobrir qual é o índice do último elemento.
#
# Exemplo:
#
# Lista: [10, 20, 30, 40, 50, 60, 70, 80]
# Quantidade de elementos: 8
# Primeiro elemento: 10
# Último elemento: 80
print("------------------------------------")
lista = [10,20,30,40,50,60,70,80]
print(f"Nossa lista completa:{lista}")
print(f"Quantidade de elementos da lista:{len(lista)}")
print(f"Primeiro elemento da lista:{lista[0]}")
print(f"Último elemento da lista:{lista[len(lista)-1]}")
print("------------------------------------")