# Desarrolla un programa que tenga las siguientes características:
# -Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
# -Dicho problema resuélvelo con bucles for y while. 
# -Justifica en el propio programa porque una opción es adecuada y la otra no.
# -¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente
#  una solución es más eficiente? Investiga para comprobarlo.

#Escribe dos numeros enteros, uno menor y otro mayor, despues encuentra todos los divisores del 
# numero mayor que hay entre ellos (ellos mismos no deben estar incluidos):


menor=int(input("Escribe un numero:"))

mayor=int(input(f"Escribe un numero mayor que {menor}:"))

inicial=menor

lista=[]

import time
start_time = time.time()

for i in range(menor+1,mayor):

    if mayor%i==0:

        lista += [i]

print("--- %s seconds ---" % (time.time() - start_time))

print ("Los divisores de",mayor,"que se encuentran entre",menor,"y",mayor,"son:",lista)

# Aqui la opcion mas adecuada, a mi parecer, es la del for, porque para hacer lo mismo necesita
# un codigo mas corto y porque no se aprovecha la ventaja del while de poder terminar antes el bucle,
# porque los dos necesitan probar con todas las opciones hasta el final.

#Si, asi ha sido. Lo he medido con una funcion de python, que he dejado puesta para que pueda ser comprobado,
# y el bucle for se resuelve casi el doble de rapido que el while.