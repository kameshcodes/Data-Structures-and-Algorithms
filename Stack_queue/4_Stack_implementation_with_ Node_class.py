# implementation of stack using linkedlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class stack:
    def __init__(self, maxSize):
        self.head = None
        self.top = 0
        self.maxSize = maxSize
        
    def __str__(self):
        current = self.head
        stack_str = ""
        while current:
            stack_str = stack_str + "\n" + str(self.head.value)
            self.head = self.head.next
            if self.head is None:
                break
        return stack_str 
        
    def isfull(self):
        if self.top==self.maxSize:
            return True
        else:
            return False
    
    def isempty(self):
        if self.top==0:
            return True 
        else:
            return False
    
    def peek(self):
        print("Top : ", self.head.value)

    def get_size(self):
        print("Size :", self.top)
        
    def push(self, value):
        new_element = Node(value)
        if self.top == self.maxSize:
            raise Exception("Stack Overflow")
        else:
            new_element.next = self.head
            self.head = new_element
            self.top+=1
            
    def pop(self):
        if self.top == 0:
            raise Exception("Stack Underflow")
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.top -=1
            return popped_node.value
        
    def delete(self):
        self.head = None
        self.top = 0
        return 
    
    
stack1= stack(maxSize=2)
stack1.push(1)
stack1.push(2)
print(stack1)
print(stack1.isempty())
print(stack1.get_size())
print(stack1.isfull())
stack1.delete()
print(stack1.get_size())
print(stack1.isempty())
print(stack1)
stack1.push(1)
stack1.push(2)
stack1.push(3)