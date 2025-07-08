## Genera los primeros n numeros primos ##
# Generando cada numero primo 

num = int(input("Ingresa tam de la lista: "))
contador = 0
generador = 2
listaPrimos = []

while contador < num:
    # Compruba si el numero es primo
    flag = True
    for i in range(2,generador):
        if generador % i == 0:
            flag = False
    
    # Agregar a la lista
    if flag == True:
        listaPrimos.append(generador)
        contador += 1

    generador += 1

for i in listaPrimos:
    print(i, end=" ")

    
