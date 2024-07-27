class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ### O(n^2)
        # i=1
        # while i < len(nums):
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)

        ### O(n)

        i = 1
        j = 0
        while i < len(nums):
            if nums[i]!=nums[j]:
                j += 1
                nums[j] = nums[i]
            i+=1
        return j+1
            