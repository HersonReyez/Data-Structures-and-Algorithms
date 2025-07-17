## Crea una lista de numeros primos de 0 hasta n ##
# Generando cada numero primo
num = int(input("Ingresa rango de la lista: "))
listaPrimos = []

for i in range(2, num):
    flag = True

    for j in range(2, i):
        if i % j == 0:
            flag = False

    if flag == True:
        listaPrimos.append(i)

for i in listaPrimos:
    print(i, end=" ")  


## Implementacion Criba de Erastostenes ##
import math

num = int(input("Ingresa rango de la lista: ")) + 1
lista = [True] * num
listaPrimos = []
RaizNum = int(math.sqrt(num)) + 1

if num > 1:
    lista[0] = False
    lista[1] = False

    # Genera los numeros primos en una lista
    for i in range(2, RaizNum):
        if lista[i] == True:
            for j in range(i + i, num, i):
                lista[j] = False

    # Crea la lista de numeros primos
    for i in range(num):
        if lista[i] == True:
            listaPrimos.append(i)


# Imprime lista
for i in listaPrimos:
    print(i, end=" ")