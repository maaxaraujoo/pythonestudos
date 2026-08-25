palavra = "Estou me divertindo muito aprendendo Python"

print("---------------------------------------------")
print(f"Frase escrita originalmente: {palavra}")
print("---------------------------------------------")
palavra_modificada = palavra.replace("Python""", "Programação")
print(f"Frase escrita com alteração, utilizando replace: {palavra_modificada}")
print(f"Frase escrita com alteração, utilizando replace MAIÚSCULA: {palavra_modificada.upper()}")
print("---------------------------------------------")
print(f"Frase escrita originalmente: {palavra}")
print("---------------------------------------------")


# QUESTÃO 8
#
# Crie uma frase contendo a palavra "Python"
# pelo menos uma vez.
#
# Depois:
#
# 1. Mostre a frase original;
# 2. Substitua "Python" por "programação";
# 3. Transforme a frase modificada em MAIÚSCULAS;
# 4. Mostre a frase final;
# 5. Mostre novamente a frase original.
#
# Utilize replace() e upper().