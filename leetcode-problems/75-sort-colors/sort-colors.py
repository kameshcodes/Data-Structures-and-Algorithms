class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  
        def swap(nums, pos1, pos2):
            temp = nums[pos1]
            nums[pos1] = nums[pos2]
            nums[pos2] = temp
            return nums
            
        for i in range(n-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums = swap(nums, j+1, j)
        return nums
        