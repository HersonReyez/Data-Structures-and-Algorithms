## Determina si un numero es primo ##
num = int(input("Ingresa numero: "))
flag = True

if num == 1:
    flag = False

for i in range(2, num):
    if num % i == 0:
        flag = False

if flag == True:
    print("Es primo")
else:
    print("No es primo")


## Determina si n numeros son primos ##
# Input: 1 2 3 4 5 
print("Ingresa lista de numeros")
lista = input()
lista = list(map(int, lista.split()))


for i in lista:
    flag = True

    if i == 1:
        flag = False

    for j in range(2, i):
        if i % j == 0:
            flag = False

    if flag == True:
        print(i, "Es primo")
    else:
        print(i, "No es primo")