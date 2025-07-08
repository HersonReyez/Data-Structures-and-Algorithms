## Genera los primeros n numeros primos ##
# Usando la Criba de Erastostenes
import math

generador = 100000
lista = [True] * generador
listaPrimos = []
RaizNum = int(math.sqrt(generador)) + 1


lista[0] = False
lista[1] = False

# Genera los numeros primos en una lista
for i in range(2, RaizNum):
    if lista[i] == True:
        for j in range(i + i, generador, i):
            lista[j] = False

# Crea la lista de numeros primos
for i in range(generador):
    if lista[i] == True:
        listaPrimos.append(i)

## Code ##
num = int(input("Ingresa tam de la lista: "))
for i in range(num):
    print(listaPrimos[i], end=" ")
