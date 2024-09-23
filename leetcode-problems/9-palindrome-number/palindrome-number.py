class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        rev_num = 0
        while x>0:
            rem = x%10
            rev_num = rev_num*10+rem
            x = x//10
        if temp==rev_num:
            return True
        else:
            False

        