# Mejoras (opcionales):
#-Que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
#-Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al
#decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe 
#dejar de jugar con nosotros.


import random

minimo=int(input("Valor minimo:"))

maximo=int(input("Valor maximo:"))

while maximo <= minimo:

    maximo=int(input("Ese numero no es mayor que el valor minimo! inserte un numero mayor como valor maximo:"))

respuesta=("")

lista=[minimo,maximo]

while respuesta != "igual":

    while respuesta == "":

        numero=random.randint(lista[0]+1,lista[-1]-1)

        respuesta=input(f"Es {numero} ?")

    while respuesta == "mayor":

        lista = [numero] + lista

        if lista[0]+1==lista[-1]:

            respuesta="igual"

        else:

            numero=random.randint(lista[0]+1,lista[-1]-1)
    
            respuesta=input(f"Es {numero} ?")

    while respuesta == "menor":

        lista = lista + [numero]

        if lista[0]+1==lista[-1]:

            respuesta="igual"

        else:

            numero=random.randint(lista[0]+1,lista[-1]-1)

            respuesta=input(f"Es {numero} ?")


if lista[0]+1==lista[-1]:

    print ("Estas haciendo trampas!! no quiero jugar con tramposos!!")

else:
    
    print ("Gracias por jugar!!")
