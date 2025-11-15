class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCostf(n, dp, cost, minCost):
            if dp[n] != -1:
                return dp[n]
            elif n == 0 or n == 1:
                dp[n] = cost[n]
                return cost[n]
            else:
                dp[n] = cost[n] + min(minCostf(n-1, dp, cost, minCost), minCostf(n-2, dp, cost, minCost))
            return dp[n]

        n = len(cost)
        dp = [-1] * (n)
        return min(minCostf(n-1, dp, cost, 0), minCostf(n-2, dp, cost, 0))
