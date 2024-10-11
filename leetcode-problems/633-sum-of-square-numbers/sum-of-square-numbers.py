class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ## Brute Force
        # for num1 in range(int(sqrt(c))+1):
        #     for num2 in range(int(sqrt(c))+1):
        #         if num1*num1 + num2*num2 == c:
        #             return True
        # return False


        if c < 0:
            return False
        
        for num1 in range(int(math.sqrt(c)) + 1):  # Start from 0 to handle cases like c = 1
            needed = c - num1 * num1
            sqrt_needed = int(math.sqrt(needed))
            if sqrt_needed * sqrt_needed == needed:
                return True
        
        return False