class BSTNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
        
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return f"The node has been inserted."

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightChild)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        import queue
        customQueue = queue.Queue()
        customQueue.put(rootNode)
        while not(customQueue.empty()):
            current_node = customQueue.get()
            print(current_node.data)
            if current_node.leftChild:
                customQueue.put(current_node.leftChild)
            if current_node.rightChild:
                customQueue.put(current_node.rightChild)
                
def searchNode(rootNode, nodeValue):
    if rootNode is None:
        print("The Value is not found.")
    elif rootNode.data == nodeValue:
        print("The Value is found.")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            print("The Value is not found.")
        elif rootNode.leftChild.data == nodeValue:
            print("The Value is found.")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild is None:
            print("The Value is not found.")
        elif rootNode.rightChild.data == nodeValue:
            print("The Value is found.")
        else:
            searchNode(rootNode.rightChild, nodeValue)
            
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print("The BST has been successfully deleted")



newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
print(insertNode(newBST, 10))
# print()
# preOrderTraversal(newBST)
# print()
# postOrderTraversal(newBST)
# print()
# InOrderTraversal(newBST)
# print()
#levelOrderTraversal(newBST)

#searchNode(newBST, 1000)

#deleteBST(newBST)


