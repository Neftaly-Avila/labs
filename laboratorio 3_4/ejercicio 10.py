def es_palindromo(frase):
    caracteres_permitidos = 'abcdefghijklmnopqrstuvwxyzáéíóú'
    frase_limpia = ''.join(c for c in frase.lower() if c in caracteres_permitidos)
    return frase_limpia == frase_limpia[::-1]

frase = input("Ingrese una frase: ")
if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")