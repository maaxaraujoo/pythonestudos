numeroPar = int(input("Digite um numero inteiro positivo:"))

cont = 1
quantidade = 0
while cont <= numeroPar:
    if cont % 2 == 0: #se for positivo
        quantidade = quantidade + 1 #aqui conta +1
    cont = cont + 1 #esse contador é o nosso rotativo, para o while funcionar

print(f"A quantidade de numeros pares é {quantidade}")
