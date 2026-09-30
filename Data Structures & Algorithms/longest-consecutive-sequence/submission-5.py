class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        l = 0

        for n in nums: 
            if n-1 not in nums: 
                t = n
                tl = 1
                while t + 1 in nums: 
                    t += 1
                    tl += 1
                l = max(tl, l)

        return l
