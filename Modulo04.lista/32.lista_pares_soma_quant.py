lista_inteiros = []
lista_pares = []
soma = 0
for cont in range (1, 9):
    entrada = int(input(f"Digite o {cont}º número inteiro:"))
    lista_inteiros.append(entrada)

    if entrada %2 == 0:
        lista_pares.append(entrada)
        soma = soma + entrada

print("---------------------------------------")
print(f"Lista de números cadastrados:{lista_inteiros}")
print(f"Lista de números cadastrados pares:{lista_pares}")
print(f"Soma dos numeros pares cadastrados:{soma}")
print(f"Quantidade de números pares cadastrados:{len(lista_pares)}")
print("---------------------------------------")
# QUESTÃO 32
#
# Desenvolva um programa que solicite ao usuário 8 números inteiros.
#
# Utilize um for para receber os números e armazená-los em uma lista.
#
# Depois que os 8 números forem cadastrados, o programa deve:
#
# 1. Mostrar a lista completa;
# 2. Mostrar somente os números pares;
# 3. Calcular a soma de todos os números pares;
# 4. Contar quantos números pares existem;
# 5. Ao final, mostrar a soma e a quantidade de números pares.
#
# Utilize:
# - input()
# - int()
# - for
# - append()
# - if
# - %
#
# Não utilize sum().
#
# Exemplo:
#
# Números cadastrados: [2, 5, 8, 3, 10, 7, 4, 1]
#
# Números pares:
# 2
# 8
# 10
# 4
#
# Soma dos pares: 24
# Quantidade de pares: 4