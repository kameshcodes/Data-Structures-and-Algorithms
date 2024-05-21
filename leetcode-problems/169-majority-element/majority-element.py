class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num] + 1

        for num in list(count.keys()):
            if count[num]>len(nums)//2:
                return num
