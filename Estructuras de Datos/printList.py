#Hola tengo mi clase Node y LinkedList
class  Node: 
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    # Constructor
    def __init__(self):
        print("List is created ! ")
        self.size = 0
        self.firstNode = None 

    # the way of add more efficent is add elements in first position
    def add(self, element):
        self.firstNode = Node(element, self.firstNode)
        self.size += 1

    #Quiero hacer una función fuera de la clase que imprima los valores de los nodos de la lista
    def printL(self, node):
        if not node:
            return
        print(node.value)
        lista.printL(node.nextNode)




#pero cuando la mando a llamar me da un error, es por qué la función no puede acceder al primer nodo de la lista?
lista = LinkedList()
lista.add(30)
lista.add(40)
lista.add(50)
lista.add(60)
lista.printL(lista.firstNode)