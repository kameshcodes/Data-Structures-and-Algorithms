class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m = len(text1)
        # n = len(text2)
        # dp = [[-1 for i in range(n+1)] for j in range(m+1)]

        # def lcs(m, n):
        #     if m==0 or n==0:
        #         return 0
            
        #     if dp[m][n] != -1:
        #         return dp[m][n]
            
        #     if text1[m-1]==text2[n-1]:
        #         dp[m][n] = 1+lcs(m-1, n-1)
        #     else:
        #         dp[m][n] =  max(lcs(m, n-1), lcs(m-1, n))
                
        #     return dp[m][n]

        # return lcs(m, n)

        
        n = len(text1)
        m = len(text2)

        t = [[-1 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    t[i][j] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[j-1] == text2[i-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[m][n]       