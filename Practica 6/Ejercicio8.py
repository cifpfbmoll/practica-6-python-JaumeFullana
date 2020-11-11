# Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números 
# introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

limite=int(input("Escribe limite:"))

valor=int(input("Escribe un valor:"))

lista=[valor]

sumavalor = 0

sumavalor += valor

while limite != sumavalor:

    valor=int(input("Escribe otro valor:"))

    sumavalor += valor

    lista += [valor]

    while sumavalor > limite:

        sumavalor -= valor

        del lista[-1]

        valor=int(input(f"{valor} es demasiado grande. Escribe otro valor:"))
        
        sumavalor += valor

        lista += [valor]

print (f"El limite a alcanzar es {limite}. La lista creada es:",end=" ")

for i in lista:

    print (i,end=", ")


