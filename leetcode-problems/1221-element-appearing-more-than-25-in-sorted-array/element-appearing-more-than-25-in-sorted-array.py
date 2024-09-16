class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for num in counter:
            if counter[num] > len(arr)//4:
                return num 