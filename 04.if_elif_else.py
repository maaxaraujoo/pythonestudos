idadepessoa = int(input("Qual a sua idade?"))

if idadepessoa < 12 :
    print("Idade de uma criança")
elif idadepessoa >= 12 and idadepessoa <= 17 :
    print("Idade de um adolescente")
else :
    print("Idade de um adulto")