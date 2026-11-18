class Solution:
    def jump(self, nums: List[int]) -> int:
        d = {}
        d[0] = 0
        b = 0
        jumps = 1
        while b < len(nums):
            for i in range(nums[b] + 1):
                if b + i in d.keys():
                    continue
                else:
                    d[b + i] = d[b] + 1
            jumps += 1
            b += 1
        return d[len(nums) - 1]

            
