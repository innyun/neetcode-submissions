class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma, mi, global_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prev_max = ma
            ma = max(num, ma * num, mi * num)
            mi = min(num, mi * num, prev_max * num)
            global_max = max(ma, global_max)
        
        return global_max

        