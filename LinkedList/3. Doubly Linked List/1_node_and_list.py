class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None 
        self.next = None
        
class doubly: 
    def __init__(self) :
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def display(self):
        if self.head is None:
            print("\nLinked List is Empty.")
        else:
            elements = []
            current_node  = self.head
            while current_node is not None:
                elements.append(current_node.value)
                current_node = current_node.next
            print(" <-> ".join(map(str, elements)))
    
    def traverse(self):
        if self.head is None:
            print("\nLinked List is Empty.")
        else:
            current_node = self.head()
            while current_node:
                print(current_node.value)
                current_node = current_node.next 
            
                
    def createDLL(self, node_value):
        new_node = Node(node_value)
        self.head = new_node 
        self.tail = new_node
        return "The linkelist has been created"
    
                
    
doubly = doubly()
print(doubly.createDLL(5))

print([node.value for node in doubly])
