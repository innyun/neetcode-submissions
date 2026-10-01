class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        t = nums[0]
        m = t
        for b in range(1, len(nums)): 
            t = max(t + nums[b], nums[b])
            m = max(m, t)
        
        return m

