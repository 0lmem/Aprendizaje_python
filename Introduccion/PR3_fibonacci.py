'''
Fibonacci con for y while
Fibonacci es una secuencia de números enteros en la que cada término es la suma de los dos anteriores.
La secuencia comienza con 0 y 1.
'''

#Fibonacci con for
print("Fibonacci con for")
num1, num2, resultado= 0, 1, 0
for i in range(18):
    print(resultado, end=" ")
    resultado = num1 + num2
    num2 = num1
    num1 = resultado    

#Fibonacci con while
print("\nFibonacci con while")
num1, num2= 0, 1
while num2 <= 1597:
    print(num1, num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2
