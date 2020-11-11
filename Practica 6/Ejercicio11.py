#Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). 
# El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego 
# el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:

import random
import time

minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))

secreto = random.randint (minimo+1, maximo-1)

print ("A ver si adivinas un número entero entre",minimo,"y",maximo,".")

numero = int(input ("Escribe un numero:"))

lista = [numero]

while numero != secreto:

    while numero > secreto:

        numero=int(input("Demasiado grande! Volver a probar: "))

        lista += [numero]

    while numero < secreto:

        numero=int(input("Demasiado pequeño! Volver a probar: "))

        lista += [numero]

print ("Correcto! Lo has intentado ",len(lista)," veces.")

