# You are required to complete this fucntion
# Function should return the an integer
def findMaxProduct(arr, n, m):
    bgn_idx, end_idx = 0, 0
	max_prod = float("-inf")
	prod = 1
	
	while end_idx<n:
		prod = prod * arr[end_idx]
		
		if end_idx-bgn_idx+1<m:
			end_idx+=1
		elif end_idx-bgn_idx+1==m:
			max_prod = max(max_prod, prod)
			prod = prod // arr[bgn_idx]
			end_idx+=1
			bgn_idx+=1
	return max_prod


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split()))
        print (findMaxProduct(arr, n, m))
# } Driver Code Ends