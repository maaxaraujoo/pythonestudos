# QUESTÃO 15
#
# Desenvolva um programa que percorra os números de 1 até 20
# utilizando um comando for.
#
# O programa deve identificar os números pares e calcular
# a soma de todos os números pares encontrados.
#
# Ao final, mostre o resultado da soma.
#
# Exemplo:
# A soma dos números pares de 1 até 20 é: 110
soma = 0
for cont in range(1, 21):
    if cont %2 == 0:
        soma = soma + cont

print(f"A soma dos numeros pares de 1 a 20 e:{soma}")

# 1 2 3 4 5 ---> 2 + 4 = 6
