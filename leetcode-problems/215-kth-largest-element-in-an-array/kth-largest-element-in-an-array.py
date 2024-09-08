import heapq as hq
class Solution:

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]

        return hq.nlargest(k, nums)[-1]


        # def heapify(idx, heap_size):
        #     n = len(nums)
        #     left = 2*idx+1
        #     right = 2*idx+2
        #     largest = idx
            
        #     if left < heap_size and nums[left] > nums[largest]:
        #         largest = left
        #     if right < heap_size and nums[right] > nums[largest]:
        #         largest = right

        #     if largest != idx:
        #         nums[idx], nums[largest] = nums[largest], nums[idx]
        #         heapify(largest, heap_size)

        # def build_heap():
        #     n = len(nums)
        #     idx = (n-2)//2
        #     while idx>=0:
        #         heapify(idx, n)
        #         idx-=1
            
        # def extract_max(heap_size):
        #     maxi = nums[0]
        #     nums[0], nums[heap_size-1] = nums[heap_size-1], None
        #     heapify(0, heap_size-1)
        #     return maxi
    

        # build_heap()
        # heap_size = len(nums)
        # for i in range(k):
        #     p = extract_max(heap_size)
        #     heap_size -= 1

        # return p    
            

