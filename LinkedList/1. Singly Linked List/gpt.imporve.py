class Node:
    def __init__(self, value):
        """
        Initialize a new node with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None  # Points to the first node in the list.
        self.tail = None  # Points to the last node in the list.
        self.length = 0   # Keeps track of the number of nodes in the list.

    def __str__(self):
        """
        Create a human-readable string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "  # Add an arrow if there's a next node.
            temp_node = temp_node.next
        return result

    def append(self, value):
        """
        Add elements to the end of the list.

        Args:
            value: The value to be added to the end of the list.
        """
        new_node = Node(value)
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
        """
        Add elements to the beginning of the list.

        Args:
            value: The value to be added to the beginning of the list.
        """
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

    def insert(self, index, value):
        """
        Add elements at a specific index in the list.

        Args:
            index: The index at which the value should be inserted.
            value: The value to be inserted.

        Returns:
            bool: True if the insertion was successful, False if the index is invalid.
        """
        if index < 0 or index > self.length:
            return False  # Invalid index, return False.

        new_node = Node(value)
        if index == 0:
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
        """
        Traverse and print the elements of the linked list.
        """
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        """
        Search for a value in the linked list.

        Args:
            target: The value to search for.

        Returns:
            str: "Exists" if the value is found, "Doesn't Exist" otherwise.
        """
        current = self.head
        while current:
            if current.value == target:
                return "Exists"
            current = current.next
        return "Doesn't Exist"

    def get(self, index):
        """
        Get the node at a specific index in the linked list.

        Args:
            index: The index of the node to retrieve.

        Returns:
            Node or None: The node at the specified index or None if the index is invalid.
        """
        if index < 0 or index >= self.length:
            return None

        current = self.head
        if index == -1:
            return self.tail
        elif index == 0:
            return self.head
        else:
            for _ in range(index - 1):
                current = current.next
            return current

    def set_value(self, index, value):
        """
        Set the value of a node at a specific index in the linked list.

        Args:
            index: The index of the node to update.
            value: The new value to set.

        Returns:
            bool: True if the update was successful, False if the index is invalid.
        """
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def pop_first(self):
        """
        Remove and return the first node in the linked list.

        Returns:
            Node or str: The removed node or "Empty List" if the list is empty.
        """
        if self.head is None:
            return "Empty List"

        if self.length == 1:
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
        """
        Remove and return the last node in the linked list.

        Returns:
            Node or str: The removed node or "Empty List" if the list is empty.
        """
        if self.length == 0:
            return "Empty List"

        popped_node = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            popped_node.next = None
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node

        self.length -= 1
        return popped_node

    def remove(self, index):
        """
        Remove and return a node at a specific index in the linked list.

        Args:
            index: The index of the node to remove.

        Returns:
            Node or int: The removed node or -1 if the index is invalid.
        """
        if index < -1  or index > self.length or self.length==0:
            return -1
        elif index == 0 and self.length!=0 :
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
            prev_node = self.get(index - 1)
            current_node = prev_node.next
            prev_node.next = current_node.next
            current_node.next = None
            self.length -= 1
            return current_node

    def delete_all(self):
        """
        Delete all nodes in the linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

# # Create an instance of the LinkedList class.
# ll = LinkedList()

# # Print the initial state of the linked list.
# print(ll)
# print(ll.head)  # Head is None as the list is empty.
# print(ll.tail)  # Tail is None as the list is empty.
# print(ll.length)  # Length is 0 as there are no elements.

# # Append an element (10) to the linked list.
# ll.append(10)
# print(ll)
# print(ll.head.value)  # Head now points to the first node with value 10.
# print(ll.tail.value)  # Tail points to the last node with value 10.
# print(ll.tail.next)  # Tail's next is None as it's the last node.
# print(ll.length)  # Length is 1 as there is one element in the list.

# # Append more elements (20, 30, 40) and insert (15) at a specific index.
# ll.append(20)
# print(ll)
# ll.append(30)
# print(ll)
# ll.prepend(40)
# print(ll)
# ll.insert(2, 25)
# print(ll)

# # Test removing nodes.
# print("Removed first node:", ll.pop_first().value)
# print(ll)
# print("Removed last node:", ll.pop().value)
# print(ll)
# print("Removed node at index 2:", ll.remove(1).value)
# print(ll)

# # Test edge cases.
# print("Removed first node:", ll.pop_first().value)
# print(ll)
# print("Removed last node:", ll.pop().value)
# print(ll)
# print("Removed node at index 0:", ll.remove(0))
# print(ll)

# # Test delete_all method.
# ll.append(10)
# ll.append(20)
# ll.append(30)
# print(ll)
# ll.delete_all()
# print("After deleting all nodes:")
# print(ll)
# print(ll.head)
# print(ll.tail)
# print(ll.length)

# # Search for a value.
# ll.append(10)
# ll.append(20)
# ll.append(30)
# print("Searching for value 20:", ll.search(20))
# print("Searching for value 40:", ll.search(40))

