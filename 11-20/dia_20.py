"""
            Bienvenido al día 20 de #100diasdepython
                    El reto de hoy es:
            De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa'
Separa las mayúsculas y minúsculas sin usar ciclos en nuevas cadenas
            e imprime el resultado en una sola línea
"""

cadena = 'PpYyTtHhOoNnIiSsTtAa'
print(cadena[0:1]+cadena[2:3]+cadena[4:5]+cadena[6:7]+cadena[8:9]+cadena[10:11]+cadena[12:13]+cadena[14:15]+cadena[16:17]+cadena[18:19])

#metodo rapido
mayusculas = cadena[::2]
print(mayusculas)