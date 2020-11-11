# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números 
# introducidos supere el límite inicial. El programa termina escribiendo la lista de números.

limite=int(input("Escribe límite:"))

valor=int(input("Escribe un valor:"))

lista = [valor]

sumavalors=0

sumavalors += valor

while limite>=sumavalors:

    valor=int(input("Escribe un valor:"))

    lista +=[valor]

    sumavalors += valor

print (f"El límite a superar es {limite}. La lista creada es",end=" ") 

for i in lista:

    print (i,end=", ")

print (f"ya que la suma de estos números es: {sumavalors}")