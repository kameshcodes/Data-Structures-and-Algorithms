class Node:
    def __init__(self, value):
        # Initialize a new node with the given value.
        self.value = value
        self.next = None

class LinkedList:
    # Initialize an empty linked list.
    def __init__(self):
        self.head = None  # Points to the first node in the list.
        self.tail = None  # Points to the last node in the list.
        self.length = 0   # Keeps track of the number of nodes in the list.
    
    def __str__(self):
        # Create a human-readable string representation of the linked list.
        # Traverse the list from the head (first node) to the end.
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
    
    # Define a prepend method to add elements to the beginning of the list.
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, set both head and tail to the new node.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, connect the new node to the current head.
            new_node.next = self.head
            # Update the head to be the new node, making it the first node.
            self.head = new_node
        self.length += 1
    
    # Define an insert method to add elements at a specific index in the list.
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False  # Invalid index, return False.
        if self.head is None:
            # If the list is empty, set both head and tail to the new node.
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            # If inserting at the beginning, connect the new node to the current head.
            new_node.next = self.head
            # Update the head to be the new node.
            self.head = new_node
        else:
            # For other positions, traverse to the node before the target index.
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            # Connect the new node to the next node in the list.
            new_node.next = temp_node.next
            # Update the next reference of the current node to point to the new node.
            temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
        current = self.head
        while current is not None:      # Time = O(n) 
            print(current.value)        # Space = O(1)
            current = current.next
    
    def search(self, target):
        current = self.head
        while current:                            # Time = O(n)
            if current.value == target:  
                return "Exists"                       # Space = O(1)
            current = current.next
        return "Doen't Exist"
    
    def get(self, index):
        current = self.head
        if index < 0 and index >= self.length:
            return  None
        elif index == -1:
            return self.tail
        elif index == 0:
            return self.head
        else: 
            for _ in range(index):
                current = current.next
            return current  
    
    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False 
    
    def pop_first(self):
        if self.head is None:
            return "Empty List"
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length==0:
            return "Empty List"
        
        popped_node = self.tail
        if self.length==1:
            self.tail = None
            self.head = None
        else:
            popped_node.next = None
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
            
        self.length-=1
        return popped_node
    
    def remove(self, index):
        if index < -1  or index > self.length:
            return -1
        if index == 0 :
            self.length-=1
            return self.pop_first()
        elif index == self.length-1 or index == -1:
            self.length-=1
            return self.pop()
        elif self.length==1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length-=1
            return temp
        else:
            # temp_node = self.head
            # for _ in range(index-1):
            #     temp_node = temp_node.next
            # current_node = temp_node.next
            # temp_node.next = current_node.next
            # current_node.next = None
            # self.length-=1
            # return "Done"
            prev_node = self.get(index-1)
            current_node = prev_node.next
            prev_node.next = current_node.next
            current_node.next = None
            self.length-=1
            return current_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length==0
    
    

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
print(ll.head.value)  # Head now points to the first node with value 5.
print(ll.tail.value)  # Tail points to the last node with value 10.
print(ll.tail.next)  # Tail's next is None as it's the last node.
print(ll.length)  # Length is 2 as there are two elements in the list.

# Append more elements (20, 30, 40) and insert (15) at a specific index.
ll.append(20)
ll.append(30)
ll.prepend(15)
ll.insert(3, 25)

# Print the state of the linked list after adding and inserting elements.
print(ll)