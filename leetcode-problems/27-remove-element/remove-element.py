class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i<length:
            if nums[i]==val:
                nums.pop(i)
                length = len(nums)
            else:
                i=i+1


        return len(nums)
        