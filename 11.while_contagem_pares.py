numeroPar = int(input("Digite um numero inteiro positivo:"))

cont = 1
quantidade = 0
while cont <= numeroPar:
    if cont % 2 == 0:
        quantidade = quantidade + 1
    cont = cont + 1 

print(f"A quantidade de numeros pares é {quantidade}")
