"""Deque is preferred over the list in the cases where we need quicker 
append and pop operations from both the ends of the container, as deque 
provides an O(1) time complexity for append and pop operations as compared
to list which provides O(n) time complexity."""

from collections import deque

class stack:
    def __init__(self, max_size = 10):
        self.list = deque()
        self.top = 0
        self.max_size = max_size
        
    def __str__(self):
        values = self.list.reverse()
        values =  [str(x) for x in self.list]
        return "\n".join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isfull(self):
        if self.top == self.max_size:
            return True
        else:
            return False
    
    def get_size(self):
        return self.top
        
    def peek(self):
        top = self.list[-1]
        print("Top: ", top)
    
    def push(self, value):
        if self.isfull():
            raise Exception("Stack Overflow")
        else:
            self.list.append(value)
            self.top += 1
            return "The element has been inserted."
    
    def pop(self):
        if self.list == []:
           raise Exception("stack underflow")
        else:
            popped_element = self.list.pop()
            self.top -= 1
            return popped_element
        
    def delete(self):
        self.list = []
        self.top = 0
        
        
stack1= stack(max_size=2)
stack1.push(1)
stack1.push(2)
stack1.peek()
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