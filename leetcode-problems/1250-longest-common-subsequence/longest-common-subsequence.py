class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1 for i in range(1001)] for j in range(1001)]
        m = len(text1)
        n = len(text2)

        def lcs(m, n):
            if m==0 or n==0:
                return 0
            
            if dp[m][n] != -1:
                return dp[m][n]
            
            if text1[m-1]==text2[n-1]:
                dp[m][n] = 1+lcs(m-1, n-1)
            else:
                dp[m][n] =  max(lcs(m, n-1), lcs(m-1, n))
                
            return dp[m][n]

        return lcs(m, n)

        