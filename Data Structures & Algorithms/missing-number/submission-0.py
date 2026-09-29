class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = 0
        t ^= len(nums)
        for i in range(len(nums)):
            t ^= i
            t ^= nums[i]
        return t
