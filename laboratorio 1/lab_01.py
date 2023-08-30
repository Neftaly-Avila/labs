#1y2 determinar y encontrar numeros primos menores que n
n = int(input("Introduce un número: "))
print("Los números primos menores que", n, "son:")

for i in range(2, n):
    es_primo = True    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    
    if es_primo:
        print(i)
#3 factorial de un numero
numero = int(input("Ingrese un número: "))
factorial = 1

while numero > 1:
    factorial *= numero
    numero -= 1

print(f"El factorial es: {factorial}")

#4 serie de fibonacci
n = int(input("Ingrese el valor de n: "))

fibonacci = [0, 1]

for i in range(2, n):
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)

print(f"Serie de Fibonacci hasta el término {n}:")
print(fibonacci)