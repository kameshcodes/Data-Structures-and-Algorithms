class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        # leader = []
        # for i in range(len(arr)-1):
        #     if arr[i]>max(arr[i+1:]):
        #         leader.append(arr[i])
                
                
        # leader.append(arr[-1])
        
        # if leader:
        #     return leader
        # return [-1]
        
        leader = []
        max_from_right = arr[-1]
        leader.append(max_from_right)
        
        i = len(arr)-2
        while i>=0:
            if arr[i]>=max_from_right:
                max_from_right = arr[i]
                leader.append(max_from_right)
            i=i-1
            
        leader.reverse()
        return leader
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends