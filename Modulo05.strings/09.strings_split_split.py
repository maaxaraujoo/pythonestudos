frase = "A vida é tão boa que esqueço as horas passarem"

palavra = frase.split()

for letra in palavra:
    if len(letra) > 4:
        print(f"{letra}")

# QUESTÃO 9
#
# Crie uma frase contendo várias palavras.
#
# 1. Transforme a frase em uma lista usando split();
# 2. Percorra essa lista utilizando for;
# 3. Dentro do for, verifique quais palavras
#    possuem mais de 4 caracteres;
# 4. Mostre somente essas palavras.
#
# Não utilize len() na frase inteira.
# A quantidade de caracteres deve ser analisada
# em cada palavra.