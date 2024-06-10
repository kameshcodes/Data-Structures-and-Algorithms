class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        ans = []
        i = 0
        j = 0
        N = len(nums)

        while j < N:
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
            if j - i + 1 > k:
                q.pop(0) 
            if j - i + 1 == k:
                ans.append(nums[q[0]]) 
                if i == q[0]:
                    q.pop(0)
                i += 1
            j += 1
        return ans
