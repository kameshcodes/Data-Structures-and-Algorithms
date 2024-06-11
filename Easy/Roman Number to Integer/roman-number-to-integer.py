#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        dict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        num = 0
        
        i = 0
        while i<len(S):
            s1 = dict[S[i]]
            if (i+1)<len(S):
                s2 = dict[S[i+1]]
                if s1>=s2:
                    num = num + s1
                    i+=1
                else:
                    num = num + (s2 - s1)
                    i+=2
            else:
                num = num + s1
                i+=1
        return num

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends