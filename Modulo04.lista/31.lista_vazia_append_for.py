nomes = []

for cont in range(1, 6):
    entrada = str(input(f"Digite {cont}º o nome:"))
    nomes.append(entrada)
print("-----------------------------------------------")
print(f"Usuários cadastrados:{nomes}")
print(f"Quantidade de nomes cadastrados:{len(nomes)}")
print("-----------------------------------------------")

# QUESTÃO 31
# Crie uma lista vazia chamada "nomes".
# Depois, utilize um for para pedir ao usuário 5 nomes.
# A cada repetição:
#
# 1. Solicite um nome utilizando input();
# 2. Adicione o nome recebido à lista utilizando append().
#
# Ao final:
#
# 3. Mostre a lista completa;
# 4. Mostre a quantidade de nomes cadastrados utilizando len().
#
# Exemplo:
#
# Digite o 1º nome: Maxwell
# Digite o 2º nome: Clara
# ...
#
# Lista de nomes: [...]
# Quantidade de nomes: 5