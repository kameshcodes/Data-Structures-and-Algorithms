#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        denominations = reversed([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000])
        
        notes = [] 
        cnt = 0
        for num in denominations:
            if int(N // num) == 0:
                continue
            cnt = N//num
            notes = notes + [num]*cnt
            N = N % num
            
        return notes


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends