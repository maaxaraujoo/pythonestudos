lista_inteiros = [2,3,6,4,11,1,8]
lista_pares = []
print("----------------------------------------")
print(f"Lista original:{lista_inteiros}")
print("----------------------------------------")

for numero in lista_inteiros:
    if numero %2 == 0:
        lista_pares.append(numero)

print(f"Lista de numeros pares: {lista_pares}")
print("----------------------------------------")
print(f"Nessa nova lista temos {len(lista_pares)} numeros pares!")
print("----------------------------------------")
print(f"Se somarmos todos os elementos dessa lista temos um total de: {sum(lista_pares)}")
print("----------------------------------------")

# QUESTÃO 37
#
# Crie uma lista com 8 números inteiros.
#
# Depois:
#
# 1. Mostre a lista original;
# 2. Verifique quais números são pares;
# 3. Coloque os números pares em uma nova lista;
# 4. Mostre a nova lista;
# 5. Mostre a quantidade de números pares usando len();
# 6. Mostre a soma dos números pares usando sum().
#
# Não precisa usar range().
#
# Use os conceitos que já aprendemos.