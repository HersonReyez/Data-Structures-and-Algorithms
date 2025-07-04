## Variables ##
num1 = 1
num2 = 2
pi = 3.1416
bandera = True
palabra1 = "Hola"
palabra2 = " Mundo"


## Entrada y salida de datos ##
nombre = input("Introduce tu nombre: ")
edad = int(input("Intoduce tu edad: ")) #Cast
print("Hola", nombre + "!", "Tienes", edad, "años.")


## Operadores ##
# Aritmeticos +, -, *, /, %
suma = num1 + num2 
frase = palabra1 + palabra2
palabra1 += palabra2 # Concatenacion

# Relacionales: <, <=, >, >=, !=, ==
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Logicos: not, and, or
if suma > 5 and bandera:
    print("Wow ! you know mathics !")


## Bucles ##
# While
contador = 0
while contador < 6:
    print(contador, end=" ") #el espacio vacio quita el salto de linea
    contador +=1
print()

# For
# range(start, end, increment)
for i in range(6):
    print(i, end=" ")
print()

for i in range(5, 11):
    print(i, end=" ")
print()

for i in range(0, 51, 10):
    print(i, end=" ")
print()

## Listas ##
listEmpty = list() # Lista vacia
listIni = [0] * 10 # Lista con 10 ceros
frutas = ["uva", "banana", "manzana", "fresa"] #Lista con contenido

## Funciones de lista
frutas.append("naranja") # Agrega al final
frutas.pop() # Elimina el último elemento
frutas.pop(1) # Elimina el segundo elemento de la
frutas.remove("fresa") # Elimina elemento especifico
print(frutas)


## Read a list 
print("Ingresa valores lista. Ejemplo: 1 2 3")
listaData = input()
lista = list(map(int, listaData.split()))


## Matrices ## 
# Inicializada
matrix = [[1,2,3], [4,5,6], [7,8,9]]

# Vacia
matrixEmpty = []
rows = 2
col = 2

print("Add vaules of matrix:")
# scan matrix
for i in range(rows):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrixEmpty.append(row)

print("Matrix:")
# print matrix
for i in range(rows):
    for j in range(col):
        print(matrixEmpty[i][j], end=" ")
    print()


## Cadenas ##
cadena = "Hola Mundo"
cadena.replace("Hola", "Adios") # remplazar
cadena.find("Mundo") #buscar


## Diccionario ##
# Agrupar datos sin lógica adicional, algo simple y rápido
# Usa internamete una tabla Hash
Animal = {
    "nombre": "Perro",
    "clase": "mamifero"
}
print(Animal["nombre"], "es un animal", Animal["clase"])

Nombres = {
    "pedro": 1,
    "oscar": 3
}
Nombres["maria"] = 0 #insertar
Nombres["maria"] += 1 #Actualizar 


## Conjuntos ##
conjunto1 = set([1,2,3,4])
conjunto1.add(5)
conjunto1.remove(5)
conjunto2 = set([3,4,5,6])
print(conjunto1.intersection(conjunto2))
# Operadores de conjuntos #
# Union A|B
# Diferencia A-B
# Superconjungto A>=B
# Interseccion A&B
# Diferencia A^B
# Subconjunto A<=B
print(conjunto1 & conjunto2)


## Funciones ##
valor = 10
def sum20(numero):
    resultado = numero + 20
    return resultado

valor = sum20(valor)


########################################################################################


## Librerias ## 
import math
print("la raiz de 16 es", math.sqrt(16))

# as sirve para renombrar
import random as r
print("Integer aleatorio entre [0, 10]:", r.randint(0,10))


## Clases ##
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear lista de personas
personas = [
    Persona("Pedro", 30),
    Persona("Juan", 22),
    Persona("Paco", 21)
]


## Funciones integradas ##
# Potencia
print("Potencia 2^3:", pow(2,3))

# Longitud  
print("El numero de personas es", len(personas))

# Suma 
suma_edades = sum(persona.edad for persona in personas)
print("La suma de las edades es", suma_edades)


## Ordenamiento ##
# No modificando la lista original y alrevez
personas_ordenadas_rev = sorted(personas, key=lambda p: p.edad, reverse=True)

# Imprimir datos personas ordenadas por edad decendiente
print("Lista de personas Decendente")
for p in personas_ordenadas_rev:
    print(p.nombre, p.edad)

# Modficando la lista original 
personas.sort(key=lambda p: p.edad)

# Imprimir datos personas ordenadas por edad acendente
print("Lista de personas Acendente")
for p in personas:
    print(p.nombre, p.edad)