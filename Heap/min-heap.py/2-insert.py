
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
    
    def insert(self, value):
        if self.size == self.capacity:
            return OverflowError
        else:
            self.size += 1
            self.arr[self.size-1] = value  #inserted in array
          
        idx = self.size - 1
        
        while idx != 0 and self.arr[idx] < self.arr[self.parent(idx)]:
            self.arr[idx], self.arr[self.parent(idx)]  = self.arr[self.parent(idx)], self.arr[idx] 
            idx = self.parent(idx)
                 
        
        
        
heap = MinHeap(5)

print(heap)
print(heap.arr)
print(heap.insert(10))
print(heap.arr)
print(heap.insert(5))
print(heap.arr)
print(heap.insert(20))
print(heap.arr)
print(heap.insert(2))
print(heap.arr)
print(heap.insert(3))
print(heap.arr)
print(heap.insert(30))
print(heap.arr)