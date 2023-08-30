
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

edades.append(edad_minima)
edades.append(edad_maxima)
print("Lista con edades añadidas:", edades)

edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 1:
    mediana = edades_ordenadas[n // 2]
else:
    mediana = (edades_ordenadas[n // 2 - 1] + edades_ordenadas[n // 2]) / 2
print("Edad mediana:", mediana)

promedio = sum(edades) / len(edades)
print("Edad promedio:", promedio)

rango_edades = edad_maxima - edad_minima
print("Rango de edades:", rango_edades)

diferencia_minimo = abs(edad_minima - promedio)
diferencia_maximo = abs(edad_maxima - promedio)
print("Diferencia entre mínimo y promedio:", diferencia_minimo)
print("Diferencia entre máximo y promedio:", diferencia_maximo)
