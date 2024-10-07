class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # max_sum = -1000
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         sum_ = sum(nums[i:j])
        #         max_sum = max(sum_, max_sum)
        # return max_sum

        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(current_sum, max_sum)
        return max_sum 