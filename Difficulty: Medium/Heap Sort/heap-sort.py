#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if i != largest:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
        return arr
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        idx = (n-2)//2
        while idx >= 0:
            self.heapify(arr, n, idx)
            idx-=1
            
        return arr
        
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        arr = self.buildHeap(arr, n)
        
        for idx in range(n-1, 0, -1):
            arr[idx], arr[0] = arr[0], arr[idx]
            arr = self.heapify(arr, idx, 0)
            
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends