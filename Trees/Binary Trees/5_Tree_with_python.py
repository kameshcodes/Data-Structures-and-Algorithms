class BinaryTreePython:
    def __init__(self, size):
        self.customList = [None]*size
        self.maxSize = size
        self.lastIndexUsed = 0
    
    def insertNode(self, nodeValue):
        if self.lastIndexUsed == self.maxSize:
            print(f"Can't Insert '{nodeValue}'. Tree is full.")
            return
        self.customList[self.lastIndexUsed] = nodeValue
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
    


tree = BinaryTreePython(5)
#(tree)

tree.insertNode(5)
tree.insertNode(3)
tree.insertNode(2)
tree.insertNode(1)
tree.insertNode(45)
tree.insertNode(5)

tree.search(5)
tree.search(15)