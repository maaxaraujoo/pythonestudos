# QUESTÃO 19
#
# Desenvolva um programa que solicite ao usuário um número inteiro positivo.
#
# Utilizando um comando for, percorra todos os números de 1 até o número informado.
#
# O programa deve:
#
# 1. Mostrar todos os números múltiplos de 3 encontrados;
# 2. Contar quantos múltiplos de 3 existem;
# 3. Ao final, mostrar a quantidade encontrada.
#
# Exemplo:
#
# Digite um número: 15
#
# Múltiplos de 3:
# 3
# 6
# 9
# 12
# 15
#
# Quantidade de múltiplos de 3: 5

quantidade = 0
numero = int(input("Digite um numero inteiro positivo:"))
print("-------------------------------------------")
print("Múltiplos de 3:")
for cont in range(1, numero + 1):
    if cont %3 == 0:
        quantidade = quantidade + 1
        print(cont)
print("-------------------------------------------")
print(f"Número digitado:{numero}")
print(f"Quantidade de Múltiplos de 3:{quantidade}")
print("-------------------------------------------")
