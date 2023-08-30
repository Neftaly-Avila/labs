
import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    try:
        if not any([incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales]):
            raise ValueError("Debes incluir al menos un tipo de carácter en la contraseña.")
        
        caracteres = ""
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiales:
            caracteres += string.punctuation
        
        generar_caracter = lambda: random.choice(caracteres)
        
        contrasena = ''.join(generar_caracter() for _ in range(longitud))
        return contrasena
    except ValueError as ve:
        return str(ve)

# Ejemplo de uso
longitud = 12
contrasena_generada = generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True)
print("Contraseña generada:", contrasena_generada)