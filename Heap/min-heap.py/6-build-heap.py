
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
            
    def minHeapify(self, idx):
        
        left = self.left_child(idx)
        right = self.right_child(idx)
        smallest = idx
        if left<self.size and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right<self.size and self.arr[right] < self.arr[smallest]:
            smallest = right 
        
        
        if smallest != idx:
            self.arr[smallest], self.arr[idx] = self.arr[idx], self.arr[smallest]
            self.minHeapify(smallest)
    
            
    def getMin(self):
        if self.size == 0:
            return "Heap is Empty"
        return self.arr[0]
    
    def extractMin(self):
        if self.size == 0:
            return "Heap is Empty"
        
        minElement = self.getMin()
        
        self.arr[0], self.arr[self.size-1]= self.arr[self.size-1], None
        self.size -= 1
        self.minHeapify(0)
        
        return minElement
    
    def decreaseKey(self, index, value):
        if self.arr[index] < value:
            raise ValueError("New value is greater than current value. Operation not allowed.")
                
        self.arr[index] = value
        i = index
        prnt = self.parent(i)
        # percolate up operation
        while i != 0 and self.arr[prnt] > self.arr[i]:
            self.arr[i], self.arr[prnt] = self.arr[prnt], self.arr[i]
            i = prnt
            prnt = self.parent(i)
            
    def increaseKey(self, index, value):
        if value < self.arr[index]:
            raise ValueError("New value is less than current value. Operation not allowed.")
        
        self.arr[index] = value
        n = len(self.arr)
        
        while index < n:
            left = self.left_child(index)
            right = self.right_child(index)
            smallest = index
            
            if right < n and self.arr[right] < self.arr[smallest]:
                smallest = right
            if left < n and self.arr[left] < self.arr[smallest]:
                smallest = left
                
            if smallest != index:
                self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
                index = smallest
            else:
                break
            
    def delete(self, index):
        inf = float('-inf')
        self.decreaseKey(index, inf)
        self.extractMin()
        
        
        
    def buildMinHeap(self, array):
        
        self.size = len(array)
        
        def Heapify(array, idx):
            left = self.left_child(idx)
            right = self.right_child(idx)
            smallest = idx
            if right < len(array) and array[right] < array[smallest]:
                smallest = right
            if left < len(array) and array[left] < array[smallest]:
                smallest = left
                           
            if smallest != idx:
                array[smallest], array[idx] = array[idx], array[smallest]
                Heapify(array, smallest)
        
        n = len(array)
        idx = (n-2)//2
    
        while idx >=0:
            Heapify(array, idx)
            idx -= 1 
            
        return array
        
        
        
        
        
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
print(heap.insert(15))
print(heap.arr)
print("-----------------------------------------------")
print(heap.extractMin())
print(heap.arr)
print("-----------------------------------------------")
heap.increaseKey(3, 40)
print(heap.arr)
# print(heap.arr)
# print("-----------------------------------------------")
# heap.delete(2)
# print(heap.arr)


# print("-----------------------------------------------")
# heap = MinHeap(5)
# nums = [15, 20, 40, 104, 24, 9, 13]
# print(heap.size)
# print(heap.buildMinHeap(nums))
# print(heap.size)
