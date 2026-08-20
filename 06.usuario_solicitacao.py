idade = int(input("Qual sua idade?"))
if idade >= 18 :
    print("Entrada Permitida")
elif idade == 16 or idade == 17:
    autori = str(input("Voce possui autorizacao?"))
    if autori == "Sim":
        print("ENTRA")
    else:
        print("NAO ENTRA")  
else:
    print("Entrada Negada")
