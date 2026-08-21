# QUESTÃO 20
#
# Desenvolva um programa que solicite ao usuário um número inteiro positivo.
#
# Utilizando um comando for, percorra todos os números de 1 até o número informado.
#
# O programa deve:
#
# 1. Identificar os números pares;
# 2. Mostrar cada número par encontrado;
# 3. Calcular a soma de todos os números pares;
# 4. Contar quantos números pares foram encontrados;
# 5. Ao final, mostrar a soma e a quantidade.
#
# Exemplo:
#
# Digite um número: 10
#
# Números pares:
# 2
# 4
# 6
# 8
# 10
#
# Soma dos números pares: 30
# Quantidade de números pares: 5

numero = int(input("Digite um numero inteiro positivo:"))

soma = 0
quant = 0
print("----Números pares encontrados:----")
for cont in range(1, numero + 1):
    if cont %2==0:
        print(cont)
        quant = quant + 1
        soma = soma + cont
print("--------------------------------------")
print(f"Soma dos numeros pares:{soma}")
print(f"Quantidade dos numeros pares:{quant}")
print("--------------------------------------")