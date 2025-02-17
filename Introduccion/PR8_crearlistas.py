'''
Ejercicio 8. Crear un programa que pida al usuario un número y cree una lista con ese número de elementos.
Posteriormente, el programa debe pedir al usuario que introduzca los elementos de la lista 
y mostrar la lista original y la suma de los elementos de la lista.
'''

# Solucion:
# Pedimos al usuario un numero de elementos para la lista.
numero_lista = input("Introduce un numero de cuantos espacios quieres en la lista:")
lista = []
SiNo = ""
# Creamos la lista con el numero de elementos que el usuario introdujo.
for i in range(int(numero_lista)):
    añadir = int(input(f"{i+1}) Introduce un numero:")) 
    lista.append(añadir) # Utilizamos el metodo append() para agregar elementos a la lista.

# Preguntamos al usuario si quiere ordenar la lista. 
# En caso de que diga no imprimimos la lista original.
while(SiNo != "si" and SiNo != "no"):
    SiNo = input("¿Quieres ordenar los elementos de la lista? (si/no): ")
    if(SiNo == "si"):
        lista.sort()
        print(f"Lista ordenada: {lista}")
    elif(SiNo == "no"):    
        print(f"\nLista original: {lista}")
    else:
        print("Opcion no valida")
        
# Imprimimos la suma de los elementos de la lista.
print(f"Suma de los numeros de la lista: {sum(lista)}")