# QUESTÃO 16
# Percorra os números de 1 até 50 utilizando um for.
# Verifique quais números são múltiplos de 5.
# Ao final, informe quantos múltiplos de 5 foram encontrados.
#
# Exemplo:
# Quantidade de múltiplos de 5: 10

quant = 0
for cont in range(1, 51):
    if cont %5==0:
        quant = quant + 1

print(f"Quantidade de múltiplos de 5: {quant}")
