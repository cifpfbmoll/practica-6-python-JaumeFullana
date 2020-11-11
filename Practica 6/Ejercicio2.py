# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, 
# simplemente escribe “Salir”. El programa termina escribiendo la lista de números.

numero = input("Escribe un numero:")

lista =[numero]

while numero!=("Salir") :

    numero = input("Escribe otro numero:")

    if numero != ("Salir"):

        lista += [numero]



print ("Los numeros que has escrito son", lista)