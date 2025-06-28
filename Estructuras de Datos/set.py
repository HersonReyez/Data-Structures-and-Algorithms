## Set ##

class  Node: 
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class Set:
    def __init__(self):
        print("Set is created ! ")
        self.size = 0
        self.firstNode = None 

    def add(self, element):
        if not self.contains(element):
            self.firstNode = Node(element, self.firstNode)
            self.size += 1

    def delete(self, element):
        if self.size > 0:
            if self.firstNode.value == element:
                self.firstNode = self.firstNode.nextNode
                self.size -= 1
            else:
                currentNode = self.firstNode
                for i in range(self.size - 1):
                    if currentNode.nextNode.value == element:
                        currentNode.nextNode = currentNode.nextNode.nextNode
                        self.size -= 1
                        break
                    currentNode = currentNode.nextNode

            
    def contains(self, element):
        currentNode = self.firstNode
        for i in range(self.size):
            if currentNode.value == element:
                return True
            currentNode = currentNode.nextNode

        return False
    
    def printSet(self):
        currentNode = self.firstNode
        for i in range(self.size):
            print(currentNode.value)
            currentNode = currentNode.nextNode

conjunto = Set()
conjunto.add(1)
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add(4)
conjunto.delete(3)
conjunto.printSet()