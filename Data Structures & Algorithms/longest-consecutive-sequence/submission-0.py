class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in nums:
                i = 0
                t = 0
                while n + i in nums:
                    t += 1
                    i += 1
                longest = max(t, longest)
            
        return longest