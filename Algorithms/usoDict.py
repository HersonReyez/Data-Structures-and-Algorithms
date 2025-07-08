#####################################
# Ejemplo de uso Dict (tabla hash)
# Codeforces C. Registration System 
#####################################
n = int(input())
nombres = {}

for _ in range(n):
    nombre = input()
    if nombre in nombres:
        nombres[nombre] += 1
        print(f"{nombre}{nombres[nombre]}")
    else:
        nombres[nombre] = 0
        print("OK")