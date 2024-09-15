class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(set(nums2))

        st1 = set(nums1)
        st2 = set(nums2)

        st = set()

        for num in st1:
            if num in st2:
                st.add(num)
        return st




        