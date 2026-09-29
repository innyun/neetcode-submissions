class Solution:
    def findMin(self, nums: List[int]) -> int:
        a, b = 0, len(nums) - 1
        while a < b:
            # m = a + (b - a) // 2
            m = (a + b) // 2
            print(a, b, m)
            if nums[b] <= nums[m]:
                a = m + 1
            else:
                b = m
        return nums[a]