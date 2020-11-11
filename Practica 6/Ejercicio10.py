# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo 
# de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre,
#  el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres 
# y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

nombre=input("Dame un nombre:")

nota=float(input("Escribe una nota:"))

lista = [[nombre, nota]]

while nota >= 0 and nota <= 10:

    nota=float(input("Escribe otra nota:"))

    lista[-1] += [nota]

del lista[-1][-1]

while nombre != "":

    nombre=input("Dame otro nombre:")

    if nombre !="":

        nota=float(input("Escribe una nota:"))

        lista.append([nombre, nota])

        while nota >= 0 and nota <= 10:

            nota=float(input("Escribe otra nota:"))

            lista[-1] += [nota]

        del lista[-1][-1]

print ("Las notas de los alumnos son:")

for i in lista:

    for j in i:

        if j==i[0]:

            print (j,end=": ")

        elif j==i[-1]:

            print (j)

        else:

            print (j,end=" - ")
