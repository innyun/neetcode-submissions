class Solution:
    def jump(self, nums: List[int]) -> int:
        b = len(nums) - 1
        steps = 0
        while b > 0:
            n = b - 1
            for a in range(b - 1, -1, -1):
                if nums[a] + a >= b:
                    n = a
            b = n
            steps += 1
        return steps
            
