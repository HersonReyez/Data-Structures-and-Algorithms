
## Librerias ## 
import math
print("la raiz de 16 es", math.sqrt(16))

# as sirve para renombrar
import random as r
print("Integer aleatorio entre [0, 10]:", r.randint(0,10))



## List like Stack ##
stack = []

# Append to top of stack - O(1)
stack.append(10)
stack.append(20)
stack.append(30)

# Pop from stack - O(1)
vaule = stack.pop()
print("Pop", vaule, "of Stack")


## List like Queue ##
from collections import deque
queue = deque()

# Append to top of queue - O(1)
queue.append(10)
queue.append(20)
queue.append(30)

# Delete from queue - O(1)
vaule = queue.popleft()
print("Delete", vaule, "of Queue")



## Conjuntos ##
conjunto1 = set([1,1,2,3])
conjunto2 = set([2,3,4])

# add & remove item into set - O(1)
conjunto1.add(5)
conjunto1.remove(5)

# lookup if item in set - O(1)
if 3 in conjunto1:
    print("3 is in set 1:")

# loop over items in set - O(n)
for x in conjunto1:
    print(x)

print("Intersection set 1 and set 2")
print(conjunto1.intersection(conjunto2))
# Operadores de conjuntos #
# Union A|B
# Diferencia A-B
# Superconjungto A>=B
# Interseccion A&B
# Diferencia A^B
# Subconjunto A<=B
print(conjunto1 & conjunto2)

# Set contruction - O(S) - S is the length of string
letters = 'aaaabbbccccdddd'
setLetters = set(letters)
print("Set of letters", setLetters)

## Counter ##
from collections import Counter
counter = Counter(letters)
print("num letters:", counter)



## Diccionario ##
# Agrupar datos sin lógica adicional, algo simple y rápido
# Usa internamete una tabla Hash
Nombres = {
    "pedro": 1,
    "oscar": 3
}

# add key and update - O(1)
Nombres["maria"] = 1 
Nombres["maria"] += 2 

# Check for presence of key in dictionary - O(1)
if "maria" in Nombres:
    print("Maria esta en el diccionario y tiene", Nombres["maria"], "puntos")

# Loop over the key:val pairs of the dictionary - O(n)
for key, val in Nombres.items():
    print(f'key {key}: val {val}')

## Defualtdict ##
from collections import defaultdict

default = defaultdict(list)
default['Puntos'] = 10
print("puntos maximos", default["Puntos"])





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


## Sorting ##
# Time complexity is O(n log n) from using Tim Sort
# Get now sorted array and reverse 
personas_ordenadas_rev = sorted(personas, key=lambda p: p.edad, reverse=True)

print("Lista de personas Decendente")
for p in personas_ordenadas_rev:
    print(p.nombre, p.edad)

# In place, modify original list
personas.sort(key=lambda p: p.edad)

print("Lista de personas Acendente")
for p in personas:
    print(p.nombre, p.edad)

# Sort array of tuples - (pos1, pos2)
tuples = [(-5,3), (2,1), (-3,-3),(7,2),(2,2)]
# t[0] sort from pos1 and t[1] sort from pos2
# if use - sorted reverse
print("Sorting tuples from second postion and reverse")
sortedTuples = sorted(tuples, key = lambda t: -t[1])
print(sortedTuples)