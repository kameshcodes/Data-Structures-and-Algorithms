class Solution:
    def duplicates(self, arr, n): 
    	# code here
    # 	arr.sort()
    # 	dup = []
    # 	i = 0
    # 	while len(arr)>1:
    # 	    if arr[-2] == arr[-1]:
    # 	        dup.append(arr[-1])
    # 	    arr.pop()
    # 	if dup:
    # 	    return sorted(list(set(dup)))
    # 	else:
    # 	    return [-1]
        maxi = max(arr)
        
        dup = {i:2 for i in range(maxi+1)}
        
        for num in arr:
            if dup[num]!=0:
                dup[num]-=1
        
        ls = [key for key in dup.keys() if dup[key]==0]
        
        if ls:
            return ls
        return [-1]
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends