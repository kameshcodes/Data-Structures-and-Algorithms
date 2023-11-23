class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.leftchild = None
        self.rightchild = None
    
    def __str__(self):
        def tree_to_str(node, level=0):
            if node is None:
                return ""
            if node.leftchild is None and node.rightchild is None:
                return "  " * level + str(node.data) + "\n"
            left_str = tree_to_str(node.leftchild, level + 1)
            right_str = tree_to_str(node.rightchild, level + 1)
            return "  " * level + str(node.data) + "\n" + left_str + right_str
        return tree_to_str(self).strip()
    
def preorderTraversal(rootnode):
    if rootnode is None:
        return 
    print(rootnode.data, end = ", ")
    preorderTraversal(rootnode.leftchild)
    preorderTraversal(rootnode.rightchild)

def postorderTraversal(rootnode):
    if rootnode is None:
        return 
    else:
        postorderTraversal(rootnode.leftchild)
        postorderTraversal(rootnode.rightchild)
        print(rootnode.data, end = ", ")
    
def inorderTraversal(rootnode):
    if rootnode is None:
        return
    else:
        inorderTraversal(rootnode.leftchild)
        print(rootnode.data, end = ", ")
        inorderTraversal(rootnode.rightchild)

def level_order_traversal(rootnode):
    from queue import Queue
    if rootnode is None:
        return []
    
    result = []
    que = Queue()
    que.put(rootnode)
    
    while not que.empty():
        current = que.get()
        result.append(current.data)
        if current.leftchild:
            que.put(current.leftchild)
        if current.rightchild:
            que.put(current.rightchild)
    print(result)
        
drink = TreeNode("Drink") # ---- Time and space complexity: O(1)

cold = TreeNode("Cold")
hot = TreeNode("Hot")
drink.leftchild = cold 
drink.rightchild = hot

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftchild = tea
hot.rightchild = coffee

coke = TreeNode("Coke")
coldcoffee = TreeNode("Cold Coffee")
cold.leftchild = coke 
cold.rightchild = coldcoffee

print()
print(drink)

print("\n\nDFS:")
print("Preorder Traversal:")
preorderTraversal(drink)
print("\n\nInorder Traversal:")
inorderTraversal(drink)
print("\n\nPostorder Traversal:")
postorderTraversal(drink)

print("\n\n\nBFS:")
print("Level Order Traversal:")
level_order_traversal(drink)
