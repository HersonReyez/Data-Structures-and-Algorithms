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
