# Desarrolla un programa que tenga las siguientes características:
# -Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
# -Dicho problema resuélvelo con bucles for y while. 
# -Justifica en el propio programa porque una opción es adecuada y la otra no.
# -¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente
#  una solución es más eficiente? Investiga para comprobarlo.

#Escribe dos numeros enteros, uno menor y otro mayor, despues encuentra todos los divisores del 
#numero mayor que hay entre ellos 

menor=int(input("Escribe un numero:"))

mayor=int(input(f"Escribe un numero mayor que {menor}:"))

divisor=menor+1

lista=[]

import time
start_time = time.time()

while divisor<mayor:

    if mayor%divisor==0:

        lista += [divisor]

        divisor+=1

    else:

        divisor+=1

print("--- %s seconds ---" % (time.time() - start_time))

print ("Los divisores de",mayor,"que se encuentran entre",menor,"y",mayor,"son:",lista)

#Justificacion en el Ejercicio14B