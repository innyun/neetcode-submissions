class Solution:
    def jump(self, nums: List[int]) -> int:
        b = 0
        furthest = nums[0]
        jumps = 0
        level_end = 0
        while b < len(nums):
            if b > level_end:
                level_end = furthest
                jumps += 1
            furthest = max(furthest, nums[b] + b)
            b += 1
        return jumps

            
