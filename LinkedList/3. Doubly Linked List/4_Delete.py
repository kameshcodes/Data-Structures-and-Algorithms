class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # Initialize length to 0

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
        self.length = 1  # Increment length to 1

    def insert(self, value, position=None):
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
                if index == position - 1:
                    break
                index += 1

            if current is None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node

        self.length += 1  # Increment length

    def search(self, target):
        if self.head is None:
            print("No Element Exist in Linked List")
        else:
            current_node = self.head
            while current_node:
                if current_node.value == target:
                    return "Found"
                current_node = current_node.next
            return "Not Found"

    def delete(self, position):
        if position < 0 or position > self.length:
            print("Invalid location. Location must be non-negative.")
            return

        if position == 0:
            if self.head.next is None:
                print("Empty DLL. Nothing to delete.")
            else:
                if position == 0:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = None

        else:
            current_node = self.head
            index = 0

            while current_node.next is not None:
                current_node = current_node.next
                if index == position - 1:
                    break
                index += 1

            if current_node.next is None:
                current_node.prev.next = None
                current_node.prev = None
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                current_node.next = None
                current_node.prev = None
        self.length -= 1 
    
    def deleteDLL(self):
        if self.head is None:
            print("Empty Linked List")
            
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next 
                
            self.head = None
            self.tail = None
            self.length = 0
            print("Linked List has been deleted")
            return
        

dll = DoublyLinkedList()
print("Length of the Doubly Linked List:", dll.length)
dll.insert(5, 0)
dll.insert(4, 0)
dll.insert(7, 2)
dll.insert(6, 2)
dll.display()
dll.delete(1)
dll.display()
print("Length of the Doubly Linked List:", dll.length)
dll.deleteDLL()
print("Length of the Doubly Linked List:", dll.length)
