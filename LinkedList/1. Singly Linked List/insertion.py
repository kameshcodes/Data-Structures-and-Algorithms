class Node:
    def __init__(self, value):
        # Create a new node with the given value.
        self.value = value
        self.next = None

class LinkedList:
    # Initialize an empty linked list.
    def __init__(self):
        self.head = None  # Points to the first node in the list.
        self.tail = None  # Points to the last node in the list.
        self.length = 0   # Keeps track of the number of nodes in the list.
    
    def __str__(self):
        # Create a string representation of the linked list.
        # Start from the head (first node) and traverse to the end.
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "  # Add an arrow if there's a next node.
            temp_node = temp_node.next
        return result
             
    # Define an append method to add elements to the end of the list.
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value.
        if self.head is None:
            # If the list is empty, set both head and tail to the new node.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, connect the last node (tail) to the new node.
            self.tail.next = new_node
            # Update the tail to be the new node, as it's now the last node.
            self.tail = new_node
        self.length += 1  # Increase the length of the list.
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next 
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
  
        
# Create an instance of the LinkedList class.
ll = LinkedList()

# Print the initial state of the linked list.
print(ll)
print(ll.head)  # Head is None as the list is empty.
print(ll.tail)  # Tail is None as the list is empty.
print(ll.length)  # Length is 0 as there are no elements.

# Append an element (10) to the linked list.
ll.append(10)
ll.prepend(5)
# Print the updated state of the linked list.
print(ll)
print(ll.head.value)  # Head now points to the first node with value 10.
print(ll.tail.value)  # Tail also points to the same node with value 10.
print(ll.tail.next)  # Tail's next is None as it's the last node.
print(ll.length)  # Length is 1 as there is one element in the list.

# Append another element (20) to the linked list.
ll.append(20)
ll.append(30)
ll.prepend(15)
ll.append(40)

# Print the state of the linked list after adding the second element.
print(ll)
