class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size-1
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        if self.rear != -1:
            lst = [str(item) for item in self.queue]
            lst.append("  <- REAR")
            lst_string = " ".join(lst)
            return lst_string
        else:
            return ""
        
    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if self.rear == self.max_size:
            return True
        else: 
            return False
    
    def peek(self):
        if self.rear == -1:
            return "Empty Queue"
        else:
            return self.queue[self.front]
    
    def enqueue(self, value):
        if  self.isFull():
            raise Exception("Queue is Full")
        else:
            self.queue.append(value)
            self.rear += 1
            if self.rear == -1:
                self.front = -1
            
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        else:
            self.queue.pop(0)
            self.rear -= 1
            if self.rear == -1:
                self.front = 0
    
    def deleteQueue(self):
        self.queue = []
        self.rear = -1
        
queue = Queue(5)
print(queue)  
print(queue.isEmpty())
queue.enqueue(5)
queue.enqueue(7) 
queue.enqueue(4)
print(queue)    
queue.dequeue()
print(queue)
print(queue.isFull())
queue.enqueue(5)
queue.enqueue(7) 
queue.enqueue(4)
print(queue)
print(queue.isFull())
queue.deleteQueue()
print(queue.isEmpty())
