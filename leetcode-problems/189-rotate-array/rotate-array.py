class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # O(n) soln
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        # return nums

        ## potential solution if inplace condition wasn't there
        # nums = nums[-k:]+nums[:-k]
        # return nums

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]