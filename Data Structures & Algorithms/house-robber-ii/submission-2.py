class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob1(nums: List[int]) -> int:
            a, b = 0, 0
            for n in nums:
                a, b = b, max(a + n, b)
            return b

        return max(rob1(nums[1:]), rob1(nums[:-1]))