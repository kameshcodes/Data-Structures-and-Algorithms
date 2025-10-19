class Solution:
    dp = {}  # class variable, shared by ALL instances

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n in Solution.dp:
            return Solution.dp[n]
        Solution.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.dp[n]
