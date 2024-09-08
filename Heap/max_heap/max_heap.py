class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.size = 0
    
    def print_heap(self):
        print(self.arr)
        
    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def insert(self, value):
        if self.size == self.capacity:
            raise MemoryError("Heap is at full Capapcity")
        
        idx = self.size
        self.arr[idx] = value
        self.size+=1
        
        while idx!=0:
            prnt = self.parent(idx)
            if self.arr[prnt] < self.arr[idx]:
                self.arr[idx], self.arr[prnt] = self.arr[prnt], self.arr[idx]
                idx = prnt
            else:
                break
            
    def maxHeapify(self, idx):
        left = self.left_child(idx)
        right = self.right_child(idx)
        largest = idx
        
        if left < self.size and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right
            
        if largest != idx:
            self.arr[largest], self.arr[idx] = self.arr[idx], self.arr[largest]
            self.maxHeapify(largest)
            
    def get_max(self):
        return self.arr[0]
    
    def extract_max(self):
        if self.size==0:
            return ValueError("Heap is Empty")
        max = self.arr[0]
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], None
        self.size = self.size-1
        self.maxHeapify(0)
        return max
    
    def increaseKey(self, idx, new_value):
        if new_value < self.arr[idx]:
            return ValueError("New value is smaller than current value. Operation not allowed.")
        
        self.arr[idx] = new_value   
        while idx!=0:
            prnt = self.parent(idx)
            if self.arr[prnt] <= self.arr[idx]:
                self.arr[prnt], self.arr[idx] = self.arr[idx], self.arr[prnt]
                idx = prnt
            else:
                break
    
    def decreaseKey(self, idx, new_value):
        if new_value >= self.arr[idx]:
            return ValueError("New value is greater than current value. Operation not allowed.")
        
        self.arr[idx] = new_value
        
        while idx < self.size:
            
            left = self.left_child(idx)
            right = self.right_child(idx)
            key = idx
            
            if left < self.size and self.arr[left]>self.arr[key]:
                key = left 
            if right < self.size and self.arr[right]>self.arr[key]:
                key = right
              
            if key != idx:
                self.arr[idx], self.arr[key] = self.arr[key], self.arr[idx]
                idx = key
            else:
                break
        
    def delete(self, index):
        inf = float('inf')
        self.increaseKey(index, inf)
        self.extract_max()
        
    def buidMaxHeap(self, array):
        self.arr = array
        self.size = len(array)
        self.capacity = len(array)+1
        
        n = len(array)
        idx = (n-2)//2 #right most internal node 
        while idx >= 0:
            self.maxHeapify(idx)
            idx -= 1
    
    
    
        
heap = MaxHeap(10)
# heap.print_heap()
# heap.insert(10)
# heap.insert(15)
# heap.insert(7)
# heap.insert(20)
# heap.insert(3)
# heap.insert(6)
# heap.insert(4)
# heap.insert(5)
# heap.insert(2)
# heap.print_heap()
# heap.extract_max()
# heap.print_heap()
# heap.increaseKey(2, 40)
# heap.print_heap()
# heap.decreaseKey(1, 1)
# heap.print_heap()
# heap.delete(2)
# heap.print_heap()
arr = [10,5, 20, 2, 4, 8]
heap.buidMaxHeap(arr)
heap.print_heap()
