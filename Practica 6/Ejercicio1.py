#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, 
#simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.

palabra = input("Escribe una palabra:")

lista =[palabra]

while palabra!=("") :

    palabra = input("Escribe más palabras:")

    if palabra != (""):

        lista += [palabra]



print ("Las palabras que has escrito son", lista)