class Solution:
    def removeDuplicates(self, s: str) -> str:
        # if len(s)==0:
        #     return ""
        # i = 0
        # while i<len(s)-1:
        #     if s[i] == s[i+1]:
        #         s = s[:i]+s[i+2:]
        #         if i>0:
        #             i -= 1
        #     else:
        #         i += 1
        # return s
        
        stack = []

        for letter in s:
            if len(stack)>0 and stack[-1] == letter:
                stack.pop() #remove the last element from the stack
            else:
                stack.append(letter)
        return "".join(stack)