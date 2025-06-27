## Modulos ##

# Importar modulo como un objeto
import mi_modulo as mo
print(mo.variable)
mo.funcion()
print()


# Importar contenido especifico del modulo
from mi_modulo import variable as va, funcion as fu
print(va)
fu()
print()

# Importar todo el contenido del modulo
from mi_modulo import *
print(variable)
funcion()
print()