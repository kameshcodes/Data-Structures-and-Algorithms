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

print(drink)

