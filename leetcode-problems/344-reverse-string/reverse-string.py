class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Cheat sols 
        return s.reverse()
        # s[:] = s[::-1] #and not s=s[::-1] modification should be inplace


        # # sol 1
        # for i in range(len(s)//2):
        #     temp = s[i]
        #     s[i] = s[(len(s)-1)-i]
        #     s[(len(s)-1)-i] = temp

        # # sol 2
        # i = 0
        # j = len(s)-1
        # while i<j:
        #     s[i], s[j] = s[j], s[i]
        #     i=i+1
        #     j=j-1



        

        
        