class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for n in nums:
            t ^= n
        return t