class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CLinkedList:
    def __init__(self, value = None):
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None 
            self.tail = None 
            self.length = 0

        