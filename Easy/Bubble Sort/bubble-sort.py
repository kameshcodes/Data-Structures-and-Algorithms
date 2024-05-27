#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        def swap(arr, pos1, pos2):
            temp = arr[pos1]
            arr[pos1] = arr[pos2]
            arr[pos2] = temp
            return arr
            
        for i in range(n-1,0,-1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr = swap(arr, j+1, j)
        return arr
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends