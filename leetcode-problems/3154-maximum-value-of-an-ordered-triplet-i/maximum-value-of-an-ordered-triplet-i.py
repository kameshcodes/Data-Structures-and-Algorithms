class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = float('-inf')
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if ((nums[i] - nums[j]) * nums[k]) > max_num:
                        max_num = ((nums[i] - nums[j]) * nums[k])
        return max_num if max_num > 0 else 0

        