class BinaryTreePython:
    def __init__(self, size):
        self.customList = [None]*size
        self.maxSize = size 
        self.lastIndexUsed = 0
    
    def insertNode(self, nodeValue):
        if self.lastIndexUsed+1 == self.maxSize:
            print(f"Can't Insert '{nodeValue}'. Tree is full.")
            return
        self.customList[self.lastIndexUsed+1] = nodeValue
        self.lastIndexUsed+=1
        print(f"Successfully Inserted '{nodeValue}' into tree")
        return
    
    def search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                print(f"'{nodeValue}' exist in tree.")
                return 
        print(f"'{nodeValue}' doesn't exist in tree.")
        return
    
    def preOrderTraversal(self, index):
        if index>self.lastIndexUsed:
            return
        print(self.customList[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)
            
    def inOrderTraversal(self, index):
        if index>self.lastIndexUsed:
            return
        self.inOrderTraversal(2*index)
        print(self.customList[index])
        self.inOrderTraversal(2*index+1)
        
    def postOrderTraversal(self,index):
        if index>self.lastIndexUsed:
            return
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.customList[index])
        
        


tree = BinaryTreePython(6)
#(tree)

tree.insertNode("Drink")
tree.insertNode("Hot")
tree.insertNode("Cold")
tree.insertNode("Tea")
tree.insertNode("Coffee")

print()
tree.preOrderTraversal(1)
print()
tree.postOrderTraversal(1)
print()
tree.inOrderTraversal(1)