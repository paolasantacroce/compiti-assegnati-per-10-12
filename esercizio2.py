parole = input("scrivere una lista di parole con la formula: parola1, parola2, ...\n")
lista_1 = parole.split(",") #ad ogni, divide la lista
lista_2 = []

for parola in lista_1:
    lunghezza = len(parola) 
    lista_2.append(lunghezza - 1)

print("La lunghezza della parola è rispettivamente di ", lista_2)