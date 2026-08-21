cont = 1
quant = 0

numero = int(input("Digite um numero inteiro e positivo:"))

while cont <= numero :
    if cont % 3 == 0:
        quant = quant + 1
    cont = cont + 1
print("-----------------------------------------------------")
print(f"Numero digitado:{numero}")
print(f"A quantidade de numeros multiplos de 3, de 1 até {numero} são: {quant}")
print("-----------------------------------------------------")
