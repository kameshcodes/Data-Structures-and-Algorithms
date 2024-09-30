#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        if n == 1: 
            return 0
            
        dp = [0 for i in range(n)]
        dp[1] = abs(height[1]-height[0])
        
        if n == 2: 
            return dp[1]
            
        

        for i in range(2, n):
            dp[i] = (min((dp[i-1]+abs(height[i]-height[i-1])), 
                        (dp[i-2]+abs(height[i]-height[i-2]))))
            
        return dp[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends