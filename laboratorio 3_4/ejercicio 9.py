Alfabeto = 'abcdefghijklmnopqrstuvwxyz'
mensaje = "abcdefghijklmnopqrstuvwxyz"
Clave = 1
cifrado = ""

for letra in mensaje:
    if letra in Alfabeto:
        indice = Alfabeto.find(letra)
        indice = (indice + Clave) % 26
        cifrado += Alfabeto[indice]
    else:
        cifrado += letra

print("Mensaje cifrado:", cifrado)