class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # O(n) soln
        # k = k % len(nums)
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        # return nums


        # k = k % len(nums) # k can be greater than l
        # nums[:] = nums[-k:] + nums[:-k]

        k = k % len(nums) 
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        