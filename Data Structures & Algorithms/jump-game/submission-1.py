class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        i = len(nums) - 1
        while i > 0:
            t = i - 1
            while t >= 0:
                if t == 0 and nums[t] >= i - t:
                    return True
                if nums[t] >= i - t:
                    break

                t -= 1
            
            i = t

        return False