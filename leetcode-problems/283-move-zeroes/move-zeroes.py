class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        while j<len(nums):
            if nums[i]==0:
                nums[:] = nums[:i]+nums[i+1:]+[nums[i]]
            else:
                i=i+1
            j=j+1
        return nums    
