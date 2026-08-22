print("---------------------------------------------------------------------")
list_frutas =["Maça","Uva","Melancia","Laranja","Limão","Mamão","Morango"]
print(f"Lista original:{list_frutas}")
print("---------------------------------------------------------------------")
para_remover = "Melancia" #temos que epecificar onde a fruta removida vai ficar
fruta_remov = list_frutas.remove(para_remover) #fruta_remov recebe None
print(f"Fruta removida:{para_remover}")
print(f"Lista alterada:{list_frutas}")
print("---------------------------------------------------------------------")

# QUESTÃO 35
#
# Crie uma lista com 7 frutas.
#
# Mostre a lista original.
#
# Depois, utilize remove() para retirar uma fruta
# específica da lista.
#
# Ao final, mostre:
#
# 1. A fruta removida;
# 2. A lista depois da remoção.
#
# Exemplo:
#
# Lista original: ["Maçã", "Uva", "Banana", "Caju", "Limão", "Melancia", "Pera"]
# Fruta removida: Banana
# Lista depois da remoção: ["Maçã", "Uva", "Caju", "Limão", "Melancia", "Pera"]