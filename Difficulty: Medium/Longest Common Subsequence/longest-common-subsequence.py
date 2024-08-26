#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        # code here
        # t = [[-1 for i in range(m+1)] for j in range(n+1)]
        
        # def lcs_helper(n, m):
        #     if n==0 or m==0:
        #         return 0
                
        #     if t[n][m]!=-1:
        #         return t[n][m]
            
        #     if str1[n-1] == str2[m-1]:
        #         t[n][m] = 1 + lcs_helper(n-1, m-1)
                
        #     else:
        #         t[n][m] = max(lcs_helper(n-1, m), lcs_helper(n, m-1))
        
        #     return t[n][m]
            
            
        # return lcs_helper(n, m)
        
        n = len(str1)
        m = len(str2)

        t = [[-1 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    t[i][j] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[j-1] == str2[i-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[m][n]       
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        str1 = str(input())
        str2 = str(input())
        ob = Solution()
        print(ob.lcs(n, m, str1, str2))

# } Driver Code Ends