# Binary Search Trees (BSTs)

# Height Balanced
class TreeNode:
    def __init__(self, vaule):
        self.vaule = vaule
        self.leftNode = None
        self.rightNode = None

A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)

A.leftNode = B
A.rightNode = C
B.leftNode = D
B.rightNode = E
C.leftNode = F
C.rightNode = G

# Binary Search Tree - O(log n)
def seachBST(node, target):
    if not node: 
        return False
    if node.vaule == target:
        return True
    
    if node.vaule > target: return seachBST(node.leftNode, target)
    else: return seachBST(node.rightNode, target)

numSeached = 9
print("Check if Vaule Exists:", numSeached)
print(seachBST(A, numSeached))
    