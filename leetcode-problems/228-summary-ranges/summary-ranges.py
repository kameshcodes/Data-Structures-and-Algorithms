class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = nums[:]
        if arr == []:
            return []
        lst = []
        start = arr[0]
        end = None
        for i in range(1, len(nums)):
            if arr[i]-arr[i-1] != 1:
                end = arr[i-1]
                if start == end:
                    lst.append(f"{start}")
                else:
                    lst.append(f"{start}->{end}")
                start = arr[i]
        if start == arr[-1]:
            lst.append(f"{start}")
        else:
            lst.append(f"{start}->{arr[-1]}")
        return lst
            
        