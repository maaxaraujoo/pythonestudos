
numero = int(input("Digite o numero para nossa soma acumulativa:"))
soma = 0
contador = 1

while contador <= numero:
    print(contador)
    soma = contador + soma
    contador = contador + 1

print(f"Valor da soma: {soma}")
