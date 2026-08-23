lista_numeros = [10, 5, 20, 5, 30, 5]

print("-------------------------------------")
print(f"Lista original: {lista_numeros}")
print(f"O número 5 apareceu {lista_numeros.count(5)} vezes.")
print(f"O maior número da lista encontrado foi: {max(lista_numeros)}")
print(f"O menor número da lista encontrado foi: {min(lista_numeros)}")
print(f"A soma de todos o números da lista é: {sum(lista_numeros)}")
lista_numeros.sort()
print(f"Todos os números da lista ordenados crescentemente:{lista_numeros}")
print("-------------------------------------")
# QUESTÃO 44
#
# Crie a seguinte lista:
#
# numeros = [10, 5, 20, 5, 30, 5]
#
# Depois:
#
# 1. Mostre a lista original;
# 2. Conte quantas vezes o número 5 aparece usando count();
# 3. Mostre o maior número usando max();
# 4. Mostre o menor número usando min();
# 5. Mostre a soma usando sum();
# 6. Ordene a lista usando sort();
# 7. Mostre a lista ordenada.
#
# Não utilize for.