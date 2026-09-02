
frasenova = "Eu venho todos os dias para a faculdade."

esta = frasenova.startswith("Eu")
print(f"Status da palavra 'Eu':{esta} ")

naoesta = frasenova.endswith(".")
print(f"Status da palavra '.':{naoesta} ")


# QUESTÃO 13
#
# Crie uma variável contendo uma frase.
#
# Depois:
#
# 1. Verifique se a frase começa com "Eu";
# 2. Mostre uma mensagem informando o resultado;
# 3. Verifique se a frase termina com ".";
# 4. Mostre uma mensagem informando o resultado.
#
# Utilize:
# - startswith()
# - endswith()
# - if/else
#
# Não utilize for.