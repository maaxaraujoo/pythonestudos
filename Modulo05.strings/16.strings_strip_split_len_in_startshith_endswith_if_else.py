fraseq16 = "  Quero sair correndo e pular no rio gelado.   "
print("+--------------------------------------------------+")
print(f"|A frase que temos é esse:{fraseq16}")
print("|--------------------------------------------------|")
#utilizei o strip() pra remover os espaços desnecessários
print(f"|Frase sem os espaços desnecessários:{fraseq16.strip()}")
print("|--------------------------------------------------|")
print(f"|Quantidade de palavras nessa frase:{len(fraseq16)}")
print("|--------------------------------------------------|")
print("|Verificando se a palavra 'Python' aparece na frase|")
if "Python" in fraseq16:
    print("|A palavra se encontra.")
else:
    print("|Essa palavra não se encontra aqui!")
print("|--------------------------------------------------|")
print("|------Verificando se a frase começa com 'Eu'------|")
fraseq16eu = fraseq16.startswith("Eu")
if fraseq16eu == True:
    print("|A frase começa com 'Eu'")
else:
    print("|A frase não começa com essa palavra")
print("|--------------------------------------------------|")
print("|------Verificando se a frase termina com '.'------|")
fraseq16ponto = fraseq16.endswith(".")
if fraseq16ponto == True:
    print("|A frase termina com '.'")
else:
    print("|A frase não termina com '.'")
print("|--------------------------------------------------|")
# QUESTÃO 16
#
# Crie uma variável contendo uma frase.
#
# Depois:
#
# 1. Mostre a frase original;
# 2. Remova os espaços desnecessários do início e do final da frase;
# 3. Mostre a frase depois do strip();
# 4. Verifique quantas palavras existem na frase;
# 5. Verifique se a palavra "Python" aparece na frase;
# 6. Verifique se a frase começa com "Eu";
# 7. Verifique se a frase termina com ".";
# 8. Mostre uma mensagem para cada uma dessas verificações.
#
# Utilize:
# - strip()
# - split()
# - len()
# - in
# - startswith()
# - endswith()
# - if/else
#
# Não utilize:
# - while
#
# Objetivo:
# Criar um programa que analise uma frase utilizando vários
# conceitos de strings que já estudamos.
#
# Atenção:
# - Para contar as palavras, considere a lista criada pelo split().
# - Nas verificações de "Python", "Eu" e ".", utilize if/else.
# - Não precisa utilizar for nesta questão.