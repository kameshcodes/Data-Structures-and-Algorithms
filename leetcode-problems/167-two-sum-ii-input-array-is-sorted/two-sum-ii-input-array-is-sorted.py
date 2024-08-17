class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            if numbers[i] in hashmap:
                return (hashmap[numbers[i]]+1, i+1)
            else:
                hashmap[target-numbers[i]] = i