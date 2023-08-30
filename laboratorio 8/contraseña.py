import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []

    if longitud < 8:
        print("La longitud mínima de la contraseña debe ser 8 caracteres.")
        return

    contrasena.append(random.choice(string.ascii_uppercase))  #letra mayúscula
    contrasena.append(random.choice(string.ascii_lowercase))  #letra minúscula
    contrasena.append(random.choice(string.digits))  #un número
    contrasena.append(random.choice(string.punctuation))  #un carácter especial

    while len(contrasena) < longitud:
        contrasena.append(random.choice(caracteres))

    random.shuffle(contrasena)
    contrasena = ''.join(contrasena)
    return contrasena

longitud_deseada = int(input("Ingresa la longitud deseada de la contraseña: "))

contrasena_segura = generar_contrasena(longitud_deseada)
print("Contraseña segura generada:", contrasena_segura)