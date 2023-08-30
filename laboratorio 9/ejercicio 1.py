
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperatura = float(input("Ingresa la temperatura: "))
        unidad = input("Ingresa la unidad (C o F): ").upper()

        if unidad == "C":
            fahrenheit = celsius_a_fahrenheit(temperatura)
            print(f"{temperatura} grados Celsius son {fahrenheit} grados Fahrenheit.")
        elif unidad == "F":
            celsius = fahrenheit_a_celsius(temperatura)
            print(f"{temperatura} grados Fahrenheit son {celsius} grados Celsius.")
        else:
            print("Por favor, ingresa una unidad válida (C o F).")

    except ValueError:
        print("Entrada incorrecta. Ingresa una temperatura válida.")

if __name__ == "__main__":
    main()
