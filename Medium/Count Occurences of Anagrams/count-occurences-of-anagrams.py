#User function Template for python3
from collections import Counter
class Solution:
	        
	def search(self,pat, txt):
	    i = 0
	    j = 0
	    count = 0
	    k = len(pat)
	    N= len(txt)
	    pat_dict = dict(Counter(pat))
	    cnt = len(pat_dict)
	    ans = 0
	    while j<N:
	        if txt[j] in pat_dict:
	            pat_dict[txt[j]]-=1
	            if pat_dict[txt[j]] == 0:
	                cnt -=1
	        
	        if j-i+1 < k:
	            j+=1
	        elif j-i+1==k:
	            if cnt == 0:
	                ans+=1
	            if txt[i] in pat_dict:
	                pat_dict[txt[i]]+=1
	                if pat_dict[txt[i]]==1:
	                    cnt+=1
	            i+=1
	            j+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code EndsCustom Input
