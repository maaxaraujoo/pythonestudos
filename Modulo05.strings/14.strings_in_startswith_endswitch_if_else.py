frasetop = "Eu estou na disciplina de Python."
print("---------------------------------------------------------------")
print(f"Frase original:{frasetop}")

print("---------------------------------------------------------------")
if "Python" in frasetop:
    print(f"A palavra 'Python' está na frase!")
else:
    print("A palavra 'Python' não está na frase!")
print("---------------------------------------------------------------")


palavraeu = frasetop.startswith("Eu")
if  palavraeu == True: #frasenova.startswith("Eu")
    print(f"A palavra 'Eu' está na frase!")
else:
    print("A palavra 'Eu' não está na frase!")
print("---------------------------------------------------------------")


palavraponto = frasetop.endswith(".")
if palavraponto == True: #frasenova.andswith(".")
    print(f"A palavra '.' está na frase!")
else:
    print("A palavra '.' não está na frase!")
print("---------------------------------------------------------------")

# QUESTÃO 14
#
# Crie uma variável contendo uma frase.
#
# Depois:
#
# 1. Mostre a frase original;
# 2. Verifique se a frase contém a palavra "Python";
# 3. Mostre uma mensagem informando se a palavra foi encontrada ou não;
# 4. Verifique se a frase começa com "Eu";
# 5. Mostre uma mensagem informando se a frase começa com "Eu";
# 6. Verifique se a frase termina com ".";
# 7. Mostre uma mensagem informando se a frase termina com ".";
#
# Utilize:
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
# Praticar diferentes formas de verificar informações
# dentro de uma string, utilizando condições.