
lista1 = set(range(1, 11))
lista2 = set(range(5, 16))
lista3 = set(range(10, 21))
print("elementos de lista 1", lista1)
print("elementos de lista 1", lista2)
print("elementos de lista 1", lista3)

conjunto_comun = lista1 & lista2 & lista3

print(conjunto_comun)
conjunto_union = lista1 | lista2 | lista3
print(conjunto_union)

conjunto_diferencia = lista1 - lista3
print(conjunto_diferencia)

tupla_comun = (min(conjunto_comun), max(conjunto_comun))
tupla_union = (min(conjunto_union), max(conjunto_union))
tupla_diferencia = (min(conjunto_diferencia), max(conjunto_diferencia))

suma_comun = sum(tupla_comun)
suma_union = sum(tupla_union)
suma_diferencia = sum(tupla_diferencia)
print(suma_diferencia)

