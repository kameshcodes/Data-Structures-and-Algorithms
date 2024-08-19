class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## TC->O(n^2), SC->O(1)
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)): 
        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit, max_profit)
        # return max_profit

        #####################################################################
        # ## TC->O(n), SC->O(n)
        # aux = []
        # for i in range(len(prices)):
        #     max_so_far = max(prices[i:])
        #     aux.append(max(prices[i:]))

        # # arr = [7,1,5,3,6,4]
        # # aux = [7,6,6,6,6,4]


        # max_profit = 0
        # for i in range(len(prices)):
        #     profit = aux[i]-prices[i]
        #     max_profit = max(profit, max_profit) 
        # return max_profit 

        #################################################################

        aux = [0 for i in range(len(prices))]
        aux[-1] = prices[-1]

        i = len(prices)-2
        while i >= 0:
            max_ = max(prices[i], aux[i+1])
            aux[i] = max_
            i = i - 1

        
        # arr = [7,1,5,3,6,4]
        # aux = [7,6,6,6,6,4]


        max_profit = 0
        for i in range(len(prices)):
            profit = aux[i]-prices[i]
            max_profit = max(profit, max_profit) 
        return max_profit 