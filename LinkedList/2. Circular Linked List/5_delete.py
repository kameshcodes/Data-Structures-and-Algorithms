class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length+=1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of Range")
        elif index == 0:   
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.tail = new_node
        self.length +=1
    
    def traverse(self):
        current = self.head
        while current is not None:    #time comlexity o(n)
            print(current.value)
            current = current.next 
            if current is self.head:
                break
        
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next 
            if current == self.head:
                break
        return False
        
    def get(self, index):
        if index < -1 or index >=self.length:
            return None 
        elif index == -1:
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        
    def set_value(self, index, value):
        current = self.get(index)
        # if current is not None:
        #     for _ in range(index):
        #         current = current.next 
        #     current.value = value
        if current:
            current.value = value
            return "Done"
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.head is None:
            return None 
        elif self.length == 1:
            self.head = None 
            self.tail = None 
            return popped_node
        else:
            self.head = self.head.next 
            self.tail.next = self.head
            popped_node.next = None 
            self.length -= 1
            return popped_node
            
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None 
        elif self.length == 1:
            self.head = self.tail =  None 
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = self.head
            self.tail = temp_node 
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def remove(self, index):
        prev_node = self.get(index-1)
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
           return self.pop_first()
        elif index == self.length-1:
           return self.pop()
        else:
             popped_node = prev_node.next
             prev_node.next = prev_node.next.next
        self.length -= 1
        return popped_node 
             
            
    def deleteall(self):
        if self.length == 0:
            return None 
        else:
            self.tail.next = None
            self.head = None
            self.tail = None
            self.length = 0
        

        
        
        
    
cll2 = CSLinkedList()
cll2.insert(0, 2)
cll2.insert(0, 1)
cll2.insert(1, 3)
cll2.insert(2, 4)
cll2.insert(4, 5)
print("List", cll2)
print("Tail Value", cll2.tail.value)
cll2.append(20)
cll2.append(30)
cll2.prepend(10)
cll2.prepend(0)
cll2.append(40)
print("List", cll2)
print("Tail Value", cll2.tail.value)


print("\ntraversing List", cll2)
cll2.traverse()

print("Searching:")
print("5" , cll2.search(5))
print("15", cll2.search(15))

print("List", cll2)
print("get value at -1", cll2.get(-1).value)
print("set value at 1", cll2.set_value(0, 500))
print("List", cll2)
cll2.set_value(3, 12200)
print("List", cll2)

print(cll2.pop_first().value)
print("List", cll2)
print(cll2.pop().value)
print("List", cll2)
print(cll2.remove(2).value)
print(cll2.remove(cll2.length-1).value)
print(cll2.remove(0).value)
cll2.deleteall()
print("List", cll2)