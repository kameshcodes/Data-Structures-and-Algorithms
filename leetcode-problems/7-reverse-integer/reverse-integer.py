class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
            
        new_num = 0
        neg = 1
        if x>0:
            i = len(str(x))-1
        else: 
            neg = -1
            i = len(str(x))-2
        x=abs(x)
        while x>0:
            last_num = x%10
            x = x//10
            new_num = new_num + 10**i*last_num
            i -= 1

        if neg*new_num >= -2**31 and neg*new_num <= 2**31 - 1:
            return neg*new_num
        else:
            return 0
