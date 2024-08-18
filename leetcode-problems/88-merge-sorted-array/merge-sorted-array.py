class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        while idx1<len(nums1) and idx2<n:
            if nums1[idx1] >= nums2[idx2]:
                nums1.insert(idx1, nums2[idx2])
                nums1.pop()
                idx2+=1
                m+=1
            elif idx1>=m:
                nums1.insert(idx1, nums2[idx2])
                nums1.pop()
                idx2+=1
            idx1+=1

        # k = m+n-1
        # i = m-1
        # j = n-1
        # while i>=0 and j>=0:
        #     if nums2[j]>=nums1[i]:
        #         nums1[k]=nums2[j]
        #         k-=1
        #         j-=1
        #     else:
        #         nums1[k] = nums1[i]
        #         k-=1
        #         i-=1
        # while j>=0:
        #     nums1[k] = nums2[j]
        #     k=k-1
        #     j=j-1