# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
# El programa termina escribiendo la lista de números:

numero=int(input("Escribe un número:"))

lista = [numero]

numero=int(input(f"Escribe un número mayor que {numero}:"))

lista += [numero]

while lista[-2] < numero:

    numero=int(input(f"Escribe un número mayor que {numero} :"))

    lista += [numero]


del lista[-1]

print ("Los números que has escrito son:",end=" ")

for i in lista:
    print (i,end=", ")
