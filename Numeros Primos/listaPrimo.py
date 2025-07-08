## Crea una lista de numeros primos de 0 hasta n ##
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
