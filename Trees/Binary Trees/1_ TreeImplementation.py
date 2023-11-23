class TreeNode:
    def __init__(self, data, childrens = []):
        self.data = data 
        self.childrens= childrens
        
    def __str__(self, level = 0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.childrens:
            ret += child.__str__(level = level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.childrens.append(TreeNode)
        
drink = TreeNode("Drink", [])

cold = TreeNode("Cold",[])
hot = TreeNode("Hot",[])

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee",[])

coke = TreeNode("Coke", [])
coldcoffee = TreeNode("Cold Coffee", [])


drink.addChild(cold)
drink.addChild(hot)

cold.addChild(coke)
cold.addChild(coldcoffee)

hot.addChild(tea)
hot.addChild(coffee)

print(drink)