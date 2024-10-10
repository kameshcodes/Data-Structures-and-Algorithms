class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0 
        right = len(s)-1        
        vowel = 'AEIOUaeiou'
        while left<right:
            if s[left] in vowel and s[right] in vowel:
                a = s[left]
                b = s[right]
                s = s[:left] + b + s[left+1:right]+ a + s[right+1:]
            elif s[left] in vowel:
                left-=1
            elif s[right] in vowel:
                right+=1
            left += 1
            right -= 1
        return s 

