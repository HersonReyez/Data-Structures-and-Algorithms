variable = "Variable de mi modulo"

def funcion():
    print("Funcion de mi modulo")

class Clase():
    def __init__(self):
        print("Clase de mi modulo")


# Al usar import este codigo se ejecuta como programa secundario
print("Este modulo hace una tarea por su cuenta")

# Para que solo se ejecute cuando sea el programa principal utilizamos:
if __name__ == "__main__":
    print("I'm main")
