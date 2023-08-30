
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("No se puede dividir entre cero.")
    return x / y

def calculator():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        choice = input("Selecciona la operación (1/2/3/4): ")

        if choice not in ['1', '2', '3', '4']:
            raise ValueError("Selección inválida. Debes elegir entre 1, 2, 3 o 4.")

        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        else:
            result = divide(num1, num2)
            operator = '/'

        print(f"Resultado: {num1} {operator} {num2} = {result}")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

calculator()