# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
# El programa termina escribiendo los dos números tal y como se pide:

numero=int(input("Escribe un numero:"))

numero2=int(input(f"Escribe un número mayor que {numero}:"))

while numero >= numero2:

    numero2=int(input(f"{numero2} no es mayor que {numero}. Vuelve a introducir un número:"))


print ("Los números que has escrito son",numero ,"y", numero2)