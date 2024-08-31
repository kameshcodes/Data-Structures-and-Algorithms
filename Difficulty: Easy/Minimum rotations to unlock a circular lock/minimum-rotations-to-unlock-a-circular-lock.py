#User function Template for python3

class Solution:
    def rotationCount(self, R, D):
        # code here
        
        rot = 0
        R = str(R)
        D = str(D)
        for i in range(len(R)):
            A = abs(int(D[i])-int(R[i]))
            K = min(int(D[i]), int(R[i])) 
            L = max(int(D[i]), int(R[i]))
            B = ((10+K)-L)
            C = abs(B)
            curr_rot = min(A, B)
            rot = rot+curr_rot
        return rot


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        R, D = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.rotationCount(R, D))
# } Driver Code Ends