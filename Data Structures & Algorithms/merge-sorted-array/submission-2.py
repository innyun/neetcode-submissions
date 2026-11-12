class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0
        for num in nums2:
            i = start
            while i < m+start and num >= nums1[i]:
                i += 1
            t = num
            prev = None
            while i < m+n:
                prev = t
                t = nums1[i]
                nums1[i] = prev
                i += 1
                if t == 0:
                    break
            start += 1
        