from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Use deque from collections for O(1) pops from the front
        ans = []
        i = 0
        j = 0
        N = len(nums)

        while j < N:
            # Maintain elements in decreasing order in the deque
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])

            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans.append(q[0])  # The front of the deque is the maximum

                # If the element at the front of the deque is the one leaving the window, remove it
                if nums[i] == q[0]:
                    q.popleft()  # Use popleft() for deque

                i += 1
                j += 1

        return ans