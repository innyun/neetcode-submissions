class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        def recurse(cur, i):
            if cur == 0:
                return True
            if i == len(nums):
                return False
            n = nums[i]
            if cur >= n and recurse(cur - n, i + 1):
                return True
            if recurse(cur, i + 1):
                return True
            return False
        
        return recurse(s // 2, 0)
        