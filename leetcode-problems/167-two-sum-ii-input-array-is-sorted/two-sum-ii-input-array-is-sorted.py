class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0 
        high = len(numbers)-1
        while low <= high:
            if numbers[low]+numbers[high]==target:
                return [low+1, high+1]
            elif numbers[low]+numbers[high] < target: #sum is small than we need to inc low 
                low +=1
            elif numbers[low]+numbers[high] > target: #sum is large decrease high
                high -= 1