class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        a, b, c = nums[0], max(nums[0], nums[1]), max(nums[1], nums[0] + nums[2])
        for i in range(3, len(nums)):
            print(a, b, c)
            a, b, c = b, c, max(c, b + nums[i], a + nums[i]) 
        return max(a, b, c)