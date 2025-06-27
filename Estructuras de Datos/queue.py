## Queue ##

class  Node: 
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class Queue:
    def __init__(self):
        print("Queue is created ! ")
        self.size = 0
        self.firstNode = None 
        self.lastNode = None

    def add(self,element):
        newNode = Node(element, None)
        if self.size == 0:
            self.firstNode = newNode
        else:
            self.lastNode.nextNode = newNode
        
        self.lastNode = newNode
        self.size += 1

    def delete(self):
        self.firstNode = self.firstNode.nextNode
        self.size -= 1

    def get(self):
        return self.firstNode.value 
    
    def printQueue(self):
        currentNode = self.firstNode
        for i in range(self.size):
            print(currentNode.value)
            currentNode = currentNode.nextNode

# Code #
cola = Queue()
cola.add(1)
cola.add(2)
cola.add(3)
cola.delete()
cola.printQueue()


