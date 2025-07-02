## Hash ##
# Con manejo de colisiones usando listas dentro de la lista

class TablaHash:
    def __init__(self, tam):
        self.tam = tam
        self.tabla = [ [] for _ in range(tam)] # Create a empty matrix 

    def funcion_hash(self, clave):
        # ord() Obtiene el valor en ASCII del caracter
        # sum() Suma los valores ASCII
        # Calculamos el indice usando la suma de los Valores ASCII
        # de los caracteres modulo el tamaño de la tabla
        return sum(ord(c) for c in clave) % self.tam
        
    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        # Añadimos el par clave-valor como una tupla 
        # en la lista del indice generado
        self.tabla[indice].append((clave,valor))

    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        #Buscamos en la lista del indice la clave
        # tupla(k, v)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
            return None
            
## CODE ##
hash_table = TablaHash(5) # create tabla hash

# Insetar valores
hash_table.insertar("gato", 10)
hash_table.insertar("perro", 20)
hash_table.insertar("tigre", 30) # posible colision

# Imprimir tabla hash
# recorrer cada lista dentro de la lista
# enumerate() devuelve pares (índice, elemento) 
for i, lista in enumerate(hash_table.tabla):
    print(f'Indice{i}: {lista}')

# Obtener el valor de una clave
print("valor de gato :", hash_table.obtener("gato"))
print("valor de tigre :", hash_table.obtener("tigre"))