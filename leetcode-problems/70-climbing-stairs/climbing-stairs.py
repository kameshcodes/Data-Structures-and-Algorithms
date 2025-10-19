class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1

        a = 1
        b = 1
        for i in range(2, n+1):
            # dp[i] = dp[i-1] + dp[i-2]
            a, b = a+b, a

        return a