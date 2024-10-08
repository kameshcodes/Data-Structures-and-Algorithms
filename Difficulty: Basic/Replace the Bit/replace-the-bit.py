#User function Template for python3
class Solution:
    def replaceBit(self, N, K):
        # code here
        if K>N.bit_length():
            return N
        return N&~(1<<(N.bit_length()-K))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k = input().strip().split(" ")
        n,k = int(n), int(k)
        ob = Solution()
        ans = ob.replaceBit(n,k)
        print(ans)
# } Driver Code Ends