fraseq15 = "Eu amo a vida, eu vivo ela como se não existisse o amanhã!"

print("----------------------------------------------------------------")
print(f"Frase original: {fraseq15}")
print("----------------------------------------------------------------")
print(f"Nessa frase a letra 'a' apareceu {fraseq15.count('a')} vezes!")
print("----------------------------------------------------------------")
print(f"Nessa frase a letra 'e' apareceu {fraseq15.count('e')} vezes!")
print("----------------------------------------------------------------")
print("Verificando se temos a palavra 'Python' na frase.....'")
if "Python" in fraseq15:
    print(f"A palavra está na frase!")
else:
    print("A palavra não está na frase")

print("----------------------------------------------------------------")

print("Verificando se a frase começa com: 'Eu'")
fraseq15eu = fraseq15.startswith("Eu")
if fraseq15eu == True:
    print("A frase começa com 'Eu'")
else:
    print("A frase não começa com 'Eu'")

print("----------------------------------------------------------------")

print("Verificando se a frase termina com: '.'")
fraseq15ponto = fraseq15.endswith(".")
if fraseq15ponto == True:
    print("A frase termina com '.'")
else:
    print("A frase não termina com '.'")

# QUESTÃO 15
#
# Crie uma variável contendo uma frase.
#
# Depois:
#
# 1. Mostre a frase original;
# 2. Verifique quantas vezes a letra "a" aparece na frase;
# 3. Verifique quantas vezes a letra "e" aparece na frase;
# 4. Verifique se a frase contém a palavra "Python";
# 5. Verifique se a frase começa com "Eu";
# 6. Verifique se a frase termina com ".";
# 7. Para cada uma das verificações, mostre uma mensagem informando o resultado.
#
# Utilize:
# - count()
# - in
# - startswith()
# - endswith()
# - if/else
#
# Não utilize:
# - for
# - while
# - split()
#
# Objetivo:
# Combinar diferentes ferramentas de strings em um único programa,
# fazendo verificações e tomando decisões com if/else.