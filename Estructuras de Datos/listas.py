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

    # the way of add more efficent is add elements in first position
    def add(self, element):
        self.firstNode = Node(element, self.firstNode)
        self.size += 1

    # add in position
    def addPos(self, position, element):
        if position <= self.size:
            if position == 0:
                self.firstNode = Node(element, self.firstNode)
            else:
                currentNode = self.firstNode
                for i in range(position - 1):
                    currentNode = currentNode.nextNode
                currentNode.nextNode = Node(element, currentNode.nextNode)
            self.size += 1
        else:
            print("Invalid position")

    # delete one element specific of list 
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
        
            
    # delete in position
    def deletePos(self, position):
        if position < self.size:
            if position == 0:
                self.firstNode = self.firstNode.nextNode
            else:
                currentNode = self.firstNode
                for i in range(position - 1):
                    currentNode = currentNode.nextNode
                currentNode.nextNode = currentNode.nextNode.nextNode
            self.size -= 1
        else:
            print("Invalid position")

    # get vaule in position 
    def get(self, position):
        if position < self.size:
            currentNode = self.firstNode
            for i in range(position):
                currentNode = currentNode.nextNode
            return currentNode.value
        else:
            print("Invalid position")

    # print list
    def printList(self):
        currentNode = self.firstNode
        for i in range(self.size):
            print(currentNode.value)
            currentNode = currentNode.nextNode

    # Functions print list using recursion
    def printListRec(self, node):
        if not node:
            return
        print(node.value)
        lista.printListRec(node.nextNode)

    def printListReverse(self, node):
        if not node:
            return
        lista.printListReverse(node.nextNode)
        print(node.value)


## Example ##
lista = LinkedList()
lista.add(30)
lista.add(40)
lista.add(50)
lista.add(60)
lista.addPos(1,10)
lista.printList()
print()
lista.delete(10)
lista.deletePos(0)
lista.printList()
print()
lista.printListRec(lista.firstNode)
print()
lista.printListReverse(lista.firstNode)