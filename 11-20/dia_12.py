"""
                Bienvenido al día 12 de #100diasdepython
                        El reto de hoy es:
Intercambia los valores de dos variables e imprime su ubicación en memoria
                        utilizando la función id()
"""


valor1 = 12
valor2 = 20

# Intercambiar los valores
temp = valor1
valor1 = valor2
valor2 = temp

# Imprimir las ubicaciones en memoria
print("Ubicación en memoria de valor1:", id(valor1))
print("Ubicación en memoria de valor2:", id(valor2))
