
## Variables ##
num1 = 2
num2 = 2
pi = 3.1416
bandera = True
palabra1 = "Hola"
palabra2 = " Mundo"


## Entrada y salida de datos ##
nombre = input("Introduce tu nombre: ")
edad = int(input("Intoduce tu edad: ")) #Cast
print("Hola", nombre + "!", "Tienes", edad, "años.")


## Assign vaules two multiple variables
vaule1 = vaule2 = 0 # same vaule
vaule1, vaule2 = 10, 20 # different vaules


## Operadores ##
# Aritmeticos +, -, *, /, %
suma = num1 + num2 
frase = palabra1 + palabra2
palabra1 += palabra2 # Concatenacion
square = 10 ** 2 # Squere number

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
frutas.insert(0, "Melon") # Agregar en posicion
frutas[0] = "sandia" # Modificar elemento
frutas.pop() # Elimina el último elemento
frutas.pop(1) # Elimina el segundo elemento de la
frutas.remove("fresa") # Elimina elemento especifico

# Check if array has an element - O(n)
if "sandia" in frutas:
    pos = frutas.index("sandia") # obtener posicion elemento
    print("sandia esta en la posicion", pos)

# print list of string with separator
print(' - '.join(frutas))

## Read a list 
print("Ingresa valores lista. Ejemplo: 2 4 5 6")
listaData = input()
lista = list(map(int, listaData.split()))
lista.sort() # Ordenamiento
print("Lista ordenada",lista)


## Cadenas ##
cadena = "Hola Mundo" #Inmutable
cadena2 = cadena.replace("Hola", "Adios") # remplazar y crea una nueva cadena
cadena.find("M") #buscar y regresa la posicion
if cadena.find("M") != -1:
    print("Ahora si", cadena)


## Matrices ## 
# Inicializada
matrix = [[1,2,3], [4,5,6], [7,8,9]]

# Vacia
matrixEmpty = []
rows = 2
col = 2

print("Add vaules of matrix: 4x4")
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


## Funciones ##
valor = 10
def sum20(numero):
    resultado = numero + 20
    return resultado

valor = sum20(valor)

# Return multiple vaules
def multiTask(vaule1, vaule2):
    mult = vaule1 * vaule2
    div = int(vaule1 / vaule2)
    return mult, div

# if you don't want receive one vaule use "_" 
# multiplation, _ = multiTask(num1, num2)
multiplation, division = multiTask(num1, num2)
print("multiTask", multiplation, division)