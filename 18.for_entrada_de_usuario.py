# QUESTÃO 16
#
# Desenvolva um programa que solicite ao usuário um número inteiro positivo.
#
# Depois, utilizando um comando for, percorra todos os números
# de 1 até o número informado.
#
# O programa deve calcular e mostrar a soma de todos os números
# pares encontrados nesse intervalo.
#
# Exemplo:
#
# Digite um número: 10
#
# A soma dos números pares de 1 até 10 é: 30
soma = 0
x = int(input("Digite um numero inteiro e positivo:"))
for cont in range(1, x + 1):
    if cont %2==0:
        soma = soma + cont
print(f"Soma de todos os numeros pares entre 1 e {x}:{soma}")

