class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob1(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            a, b = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                a, b = b, max(a + nums[i], b)
            return max(a, b)

        return max(rob1(nums[1:]), rob1(nums[:-1]))