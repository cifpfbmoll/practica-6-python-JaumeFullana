#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. 
#Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
#El programa termina escribiendo la lista de números.

numero1=int(input("Escribe un número:"))

numero2=int(input(f"Escribe un número mayor que {numero1}:"))

while numero1 >= numero2: 
    
    numero2=int(input(f"{numero2} no es mayor que {numero1}. Vuelve a probar:"))

numeroint=int(input(f"Escribe un número entre {numero1} y {numero2}:"))

lista = [numeroint]

while numeroint>numero1 and numeroint<numero2:

    numeroint=int(input(f"Escribe un número entre {numero1} y {numero2}:"))

    lista += [numeroint]

del lista[-1]

print (f"Los números situados entre {numero1} y {numero2} que has escrito son:",end=" ")

for i in lista:

    print (i,end=", ")