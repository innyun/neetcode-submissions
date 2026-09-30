class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        suf = [1] * l

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [pre[i] * suf[i] for i in range(l)]