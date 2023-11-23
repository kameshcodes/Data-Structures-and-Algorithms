class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None 
        self.next = None
        
class DoublyLinkedList: 
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
            print("\nLinked List is Empty. Nothing to Display")
        else:
            elements = []
            current = self.head
            while current is not None:
                elements.append(current.value)
                current = current.next
            print(" <-> ".join(map(str, elements)))
            
    def traverse(self):
        if self.head is None:
            print("\nLinked List is Empty. Nothing to Traverse")
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next
                
    def reverse_traverse(self):
        if self.head is None:
            print("\nLinked List is Empty. Nothing to Traverse")
        else:
            current_node = self.tail
            while current_node:
                print(current_node.value)
                current_node = current_node.prev
    
    def createDLL(self, node_value):
        new_node = Node(node_value)
        self.head = new_node 
        self.tail = new_node

    def insert(self, value, position = None):
        new_node = Node(value)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node 
                self.head = new_node
        else:
            current = self.head
            index = 0
            
            while current is not None:
                current = current.next 
                if index == position-1:
                    break
                index +=1
                
            if current is None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                new_node.prev = current.prev
                new_node.next = current 
                current.prev.next = new_node
                current.prev = new_node

dll = DoublyLinkedList()
dll.display()
dll.traverse()
dll.insert(5,0)
dll.insert(4,0)
dll.insert(7,2)
dll.insert(6,2)
dll.traverse()
dll.display()
#dll.traverse()
dll.reverse_traverse()


