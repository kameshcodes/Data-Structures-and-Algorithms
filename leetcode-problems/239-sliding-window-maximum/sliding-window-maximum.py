class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        ans = []
        i = 0
        j = 0
        N = len(nums)

        while j < N:
            # while q and nums[q[-1]] <= nums[j]:
            while q and q[-1] < nums[j]:
                q.pop()
            # q.append(j)
            q.append(nums[j])
            if j - i + 1 == k:
                ans.append(q[0]) 
                # ans.append(nums[q[0]]) 
                if nums[i] == q[0]:
                    q.pop(0)
                i += 1
            j += 1

        return ans
