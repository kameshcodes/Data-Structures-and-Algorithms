#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        if K == 0:
            return (sum(candies), sum(candies))
        if N == 0:
            return (0, 0)
            
            
        min_candies = sorted(candies)
        max_candies = sorted(candies, reverse = True)
        
        #min price
        min_price = 0
        max_price = 0
        while len(min_candies)>0:
            max_price+=max_candies.pop(0)
            min_price+=min_candies.pop(0)
            
            if len(max_candies) >= K:
                min_candies = min_candies[:-K]
                max_candies = max_candies[:-K]
            else:
                break

        return (min_price, max_price)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends