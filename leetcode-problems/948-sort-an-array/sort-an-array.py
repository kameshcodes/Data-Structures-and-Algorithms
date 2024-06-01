class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1

        def merge(nums, low, mid, high):
            left = low
            right = mid+1
            lst = []
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    lst.append(nums[left])
                    left+=1
                else:
                    lst.append(nums[right])
                    right+=1

            while left<=mid:
                lst.append(nums[left])
                left+=1

            while right<=high:
                lst.append(nums[right])
                right+=1
            
            for i in range(low, high+1):
                nums[i] = lst[i-low]
            return nums


        def mergesort(nums, low, high):
            if len(nums)==1 or len(nums)==0:
                return nums
            if low>=high:
                return

            mid = (low+high)//2
            mergesort(nums, low, mid)
            mergesort(nums, mid+1, high)
            nums = merge(nums, low, mid, high)
            return nums

        return mergesort(nums, low, high)