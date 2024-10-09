class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        nums.sort()
        while i<n-1:
            if nums[i]==nums[i+1]:
                return nums[i]
            i+=1
        return -1


        