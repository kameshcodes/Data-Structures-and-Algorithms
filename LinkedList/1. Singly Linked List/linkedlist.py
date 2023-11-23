# Node doesn't know anything more than its value and address to next node 
# Thats why we are creating a seperate node for that
# initially we dont about next node as well so keep none
# time complexity for init is O(1), space complexity is also O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# # This line creates an object of Node class named as 'new_node'
# # initialize its variable 'value to 10' and 'next to None'
# new_node = Node(10)
# # print the memory location (reference) of the 'new_node' object.
# print(new_node) 
# # Print the value stored in the 'value' attribute of 'new_node'.
# print(new_node.value)



# time complexity for init is O(1), space complexity is also O(1)
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)    # O(1)
        self.head = new_node      # O(1)
        self.tail = new_node      # O(1)
        self.length = 1       
# # Create a new object of the LinkedList class called 'new_linked_list' with a value of 20.
# # This value is assigned to the 'value' attribute of the initial node, 'new_node'.
# new_linked_list = LinkedList(20)
# # Print the reference location of the 'new_linked_list' object.
# print(new_linked_list)
# # Print the reference to 'head' of the linked list, which is the location of 'new_node'.
# print(new_linked_list.head)
# # Print the value stored in the 'value' attribute of the 'head' node within the 'new_linked_list'.
# print(new_linked_list.head.value)





# Define a LinkedList2 class to create an empty linked list.
class LinkedList2:
    def __init__(self):
        # Initialize both 'head' and 'tail' attributes to None,
        # indicating an empty linked list.
        self.head = None
        self.tail = None