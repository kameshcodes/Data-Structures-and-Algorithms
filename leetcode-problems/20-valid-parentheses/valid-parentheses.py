class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        para = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for element in s:
            if len(lst)==0:
                lst.append(element)
                continue
            if element in para:
                if lst[-1]==para[element]:
                    lst.pop()
                    continue
            lst.append(element)

        if len(lst)==0:
            return True
        else:
            return False
                
        