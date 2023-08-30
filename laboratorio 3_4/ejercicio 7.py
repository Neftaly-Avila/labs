
def contar_caracteres_palabras(frase):
    caracteres_totales = len(frase)
    palabras = frase.split()
    num_palabras = len(palabras)
    
    return caracteres_totales, num_palabras

frase = "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"
caracteres, palabras = contar_caracteres_palabras(frase)

print(f"Número de caracteres: {caracteres}")
print(f"Número de palabras: {palabras}")
