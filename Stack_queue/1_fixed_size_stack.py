class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size-1
        
    def __str__(self):
        if self.isempty():
            return ""
        else:
            lst =  [str(item) for item in self.stack]
            lst.append("  <- Top")
            lst = " ".join(lst)
            return lst
            
    def isempty(self):
        if self.stack == []:
            return True
        else:
            return False
        
    def isfull(self):
        if self.top > self.max_size:
            return True
        else:
            return False
    
    def get_size(self):
        print("Size of the Stack is ", self.top + 1)
        
    def peek(self):
        top = self.stack[-1]
        print("Object at Top of Stack: ", top)
    
    def push(self, value):
        if self.isfull():
            raise Exception("Stack Overflow")
        else:
            self.stack.append(value)
            self.top += 1
            return "The element has been inserted."
    
    def pop(self):
        if self.isempty():
           raise Exception("stack underflow")
        else:
            popped_element = self.stack.pop()
            self.top -= 1
            return popped_element
        
    def delete(self):
        self.stack = []
        self.top = 0
        
        
stack1= Stack(max_size=2)
stack1.push(1)
stack1.push(4)
stack1.get_size()
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
print(stack1)