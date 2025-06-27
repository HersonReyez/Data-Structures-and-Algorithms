## List ##

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

    # add in position
    def add(self, position, element):
        if position == 0:
            self.firstNode = Node(element, self.firstNode)
        else:
            currentNode = self.firstNode
            for i in range(position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = Node(element, currentNode.nextNode)

        self.size += 1

    # delete in position
    def delete(self, position):
        if position == 0:
            self.firstNode = self.firstNode.nextNode
        else:
            currentNode = self.firstNode
            for i in range(position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = currentNode.nextNode.nextNode

        self.size -= 1

    # get vaule in position 
    def get(self, position):
        currentNode = self.firstNode
        for i in range(position):
            currentNode = currentNode.nextNode
        return currentNode.value

    def printList(self):
        currentNode = self.firstNode
        for i in range(self.size):
            print(currentNode.value)
            currentNode = currentNode.nextNode
            

## Example ##
lista = LinkedList()
lista.add(0, 20)
lista.add(1, 25)
lista.add(2, 27)
lista.add(3, 30)
lista.delete(3)

lista.printList()





