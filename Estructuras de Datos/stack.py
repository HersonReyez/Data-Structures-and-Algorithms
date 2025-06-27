## Stack ##

class  Node: 
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class Stack:
    def __init__(self):
        print("Stack is created ! ")
        self.size = 0
        self.firstNode = None 
    
    def add(self, element):
        self.firstNode = Node(element, self.firstNode)
        self.size += 1

    def delete(self):
        self.firstNode = self.firstNode.nextNode
        self.size -= 1

    def get(self):
        return self.firstNode.value 
    
    def printStack(self):
        currentNode = self.firstNode
        for i in range(self.size):
            print(currentNode.value)
            currentNode = currentNode.nextNode

# Code #
pila = Stack()
pila.add(1)
pila.add(2)
pila.add(3)
pila.delete()
pila.printStack()