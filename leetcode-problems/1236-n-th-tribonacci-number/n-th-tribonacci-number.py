class Solution:
    def tribonacci(self, n: int) -> int:
        # dp = [0] * (n+1)
        # dp[0:2] = [0, 1, 1]

        # if n<3:
        #     return dp[n]
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        # return dp[n]

        memo = {}
        def count(n, memo):
            if n in memo:
                return memo[n]
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            else:
                memo[n] = count(n-1, memo) + count(n-2, memo) + count(n-3, memo)
                return memo[n]
        
        return count(n, memo)


