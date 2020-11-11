#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número 
#se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.

import random

minimo=int(input("Valor minimo:"))

maximo=int(input("Valor maximo:"))

respuesta=("")

lista=[minimo,maximo]

while respuesta != "igual":

    while respuesta == "":

        numero=random.randint(lista[0]+1,lista[-1]-1)

        respuesta=input(f"Es {numero} ?")

    while respuesta == "mayor":

        lista = [numero] + lista

        numero=random.randint(lista[0]+1,lista[-1]-1)
        
        respuesta=input(f"Es {numero} ?")

    while respuesta == "menor":

        lista = lista + [numero]

        numero=random.randint(lista[0]+1,lista[-1]-1)

        respuesta=input(f"Es {numero} ?")


print ("Gracias por jugar!!")

