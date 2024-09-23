class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        new_num = 0
        while x>0:
            rem = x%10
            new_num = new_num*10+rem
            x = x//10
        if y==new_num:
            return True
        else:
            False

        