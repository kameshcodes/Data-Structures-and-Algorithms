class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp = {}
        def countWays(n):
            if n in dp:
                return dp[n]
            elif n==0 or n==1:
                return 1
            else:
                dp[n] = countWays(n-1)+countWays(n-2)
                return dp[n]
        return countWays(n)