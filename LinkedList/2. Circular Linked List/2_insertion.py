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
            print(Exception)
            return -1
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
    
        
        
        
# cll = CSLinkedList()

# cll.append(20)
# print(cll)
# cll.append(30)
# print(cll)
# cll.prepend(10)
# print(cll)
# cll.prepend(0)
# print(cll)
# cll.append(40)
# print(cll)

cll2 = CSLinkedList()
cll2.insert(0, 2)
print(cll2)
cll2.insert(0, 1)
print(cll2)
cll2.insert(1, 3)
print(cll2)
cll2.insert(2, 4)
print(cll2)
cll2.insert(4, 5)
print(cll2)


