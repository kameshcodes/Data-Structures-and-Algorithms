class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        while right<=len(nums)-1:
            if nums[right-1] != nums[right]:
                nums[left] = nums[right]
                left = left + 1
            right = right + 1
        return left

