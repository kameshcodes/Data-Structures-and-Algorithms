class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        maxi = float('-inf')

        for i in range(len(nums)):
            if sum_ < 0:
                sum_ = 0
            sum_ = sum_ + nums[i]
            
            if sum_ > maxi:
                maxi = sum_

        return maxi
