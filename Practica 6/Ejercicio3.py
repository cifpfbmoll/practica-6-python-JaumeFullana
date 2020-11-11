# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, 
# escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.

nota=float(input("Escribe una nota:"))

lista=[nota]

while nota>=0 and nota<=10:

    nota=float(input("Escribe una nota:"))

    lista += [nota]

del lista[-1]

print ("Las notas que has escrito son", lista)