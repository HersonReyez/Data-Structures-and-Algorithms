## Binary Tree ##

class TreeNode:
    def __init__(self, vaule):
        self.vaule = vaule
        self.leftNode = None
        self.rightNode = None

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.leftNode = B
A.rightNode = C
B.leftNode = D
B.rightNode = E
C.leftNode = F

# Iterative Pre Order Traversal (DFS) - O(n)
def DFSwithStack(node):
    stack = [node]
    while stack:
        treeNode = stack.pop()
        if treeNode.rightNode: stack.append(treeNode.rightNode)
        if treeNode.leftNode: stack.append(treeNode.leftNode)
        print(treeNode.vaule)

print("DFS - Preorder with Stack")
DFSwithStack(A)

# Recursive Pre Order Traversal (DFS) - O(n)
def dfs_preorder(node):
    if not node:
        return
    
    print(node.vaule)
    dfs_preorder(node.leftNode)
    dfs_preorder(node.rightNode)
    
print("DFS - Preorder")
dfs_preorder(A)

# Recursive In Order Traversal (DFS) - O(n)
def dfs_inorder(node):
    if not node:
        return
    
    dfs_inorder(node.leftNode)
    print(node.vaule)
    dfs_inorder(node.rightNode)

print("DFS - Inorder")
dfs_inorder(A)

# Recursive Post Order Traversal (DFS) - O(n)
def dfs_postorder(node):
    if not node:
        return
    
    dfs_postorder(node.leftNode)
    dfs_postorder(node.rightNode)
    print(node.vaule)

print("DFS - Postorder")
dfs_postorder(A)

# Level Order Traversal (BFS) - O(n)
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        treeNode = queue.popleft()
        print(treeNode.vaule)
        if treeNode.leftNode: queue.append(treeNode.leftNode)
        if treeNode.rightNode: queue.append(treeNode.rightNode)

print("BFS - level Order")
bfs(A)
        
# Check if Value Exists (DFS) - O(n)
def seach(node, target):
    if not node: 
        return False
    if node.vaule == target:
        return True
    
    return seach(node.leftNode, target) or seach(node.rightNode, target)

numSeached = 20
print("Check if Vaule Exists:", numSeached)
print(seach(A, numSeached))