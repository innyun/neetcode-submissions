class Solution:
    def findMin(self, nums: List[int]) -> int:
        a, b = 0, len(nums) - 1
        while a < b:
            m = (a + b) // 2
            if nums[b] > nums[m]:
                b = m
            else:
                a = m + 1
        return nums[a]