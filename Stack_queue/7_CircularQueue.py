class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            items = []
            i = self.front
            while True:
                items.append(str(self.queue[i]))
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            items.append("  <- REAR")
            return " ".join(items)

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.max_size == self.front

    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.queue[self.front]

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is Full")
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        else:
            self.front = (self.front + 1) % self.max_size

    def deleteQueue(self):
        self.queue = [None] * self.max_size
        self.front = 0
        self.rear = 0

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

