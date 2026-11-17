class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        furthest = 0
        while i < len(nums):
            if i > furthest:
                return False
            else:
                furthest = max(furthest, i + nums[i])
            i += 1
        
        return furthest >= len(nums) - 1