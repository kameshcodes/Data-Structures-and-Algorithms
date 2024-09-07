class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.size = 0
    
    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2
        
        
heap = MinHeap(5)

print(heap)
print(heap.arr)
print(heap.left_child(3))
