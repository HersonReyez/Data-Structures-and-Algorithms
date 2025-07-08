## Recurvidad #

# Ejemplo Sumatoria de una lista
# Version iterativa
lista = [50, 100, 150, 70, 250]

total = 0
for suma in lista:
    total += suma
print("La suma de la lista es ", total)

# Version Recursiva
def sumaLista(suma):
    if len(suma) == 1:
        return suma[0]
    
    return suma[0] + sumaLista(suma[1:])

totalRec = sumaLista(lista)
print("La suma de la lista es ", totalRec)

## Ejemplo Recurion Indirecta ##
def ping(x):
    if x > 10:
        #END
        return
    print("ping", x)
    pong(x+1)

def pong(x):
    if x > 10:
        #END
        return
    print("pong", x)
    ping(x+1)

ping(1)



