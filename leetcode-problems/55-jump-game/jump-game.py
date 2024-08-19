class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-1
        reachable = i
        while i>0:
            i -= 1
            can_jump_here = nums[i] + i
            if reachable <= can_jump_here:
                reachable = i
            
        if reachable == 0:
                return True
        return False