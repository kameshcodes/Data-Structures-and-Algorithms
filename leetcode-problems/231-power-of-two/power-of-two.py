import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        p = math.log2(n)
        return p.is_integer()
        