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
    
cll2 = CSLinkedList()
cll2.insert(0, 2)
cll2.insert(0, 1)
cll2.insert(1, 3)
cll2.insert(2, 4)
cll2.insert(4, 5)
cll2.append(20)
cll2.append(30)
cll2.prepend(10)
cll2.prepend(0)
cll2.append(40)

# cll2.traverse()
# print(cll2.search(5))
# print(cll2.search(15))

print(cll2)

print(cll2.get(-1).value)
print(cll2.get(1).value)
cll2.set_value(-1, 100)
print(cll2)
cll2.set_value(0, 500)
print(cll2)
cll2.set_value(3, 12200)
print(cll2)
