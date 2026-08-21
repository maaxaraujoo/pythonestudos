


nota1 = int(input("Informe a primeira nota do aluno:"))
nota2 = int(input("Informe a segunda nota do aluno:"))

media = 0
media = (nota1 + nota2)/2

print(f"----A media do aluno e:{media}----")

if media >= 7:
    print("Aprovado")
elif media >= 5 and media<7:
    print("Recuperacao")
else:
    print("Reprovado")
