lista_numeros = []
lista_numeros_pares = []
print(f"-----Lista de números inteiros-----")
for numero in range(1, 9):
    x = int(input(f"Insira o {numero}º número: "))
    lista_numeros.append(x)
    if x %2==0:
        lista_numeros_pares.append(x)
print("-------------------------IMPRESSÕES--------------------------")
print(f"Lista formada de números: {lista_numeros}")
print("-------------------------------------------------------------")
print(f"Lista formada de números pares: {lista_numeros_pares}")
print(f"Foram encontrados {len(lista_numeros_pares)} números pares.")
soma_par = sum(lista_numeros_pares)
print(f"A soma de todos o números pares da lista é: {(soma_par)}")
print(f"O maior número da lista encontrado foi: {max(lista_numeros)}")
print(f"O menor número da lista encontrado foi: {min(lista_numeros)}")
lista_numeros.sort()
print(f"Lista completa em ordem crecente: {lista_numeros}")
lista_numeros.reverse()
print(f"Lista completa em ordem decrescente: {lista_numeros}")
print("-------------------------------------------------------------")

# QUESTÃO 45
#
# Crie uma lista vazia chamada lista_numeros.
# 1. Utilize append() para cadastrar 8 números inteiros
#    informados pelo usuário.
# 2. Mostre a lista completa.
# 3. Crie uma segunda lista contendo somente os números pares.
# 4. Mostre essa segunda lista.
# 5. Mostre quantos números pares foram encontrados.
# 6. Mostre a soma dos números pares.
# 7. Mostre o maior número da lista original.
# 8. Mostre o menor número da lista original.
# 9. Ordene a lista original em ordem crescente.
# 10. Depois, inverta a lista para deixá-la em ordem decrescente.
# 11. Mostre a lista final.
#
# IMPORTANTE:
# Não vou indicar qual função/método você deve usar
# em cada etapa.
#
# Use tudo que você aprendeu sobre listas.