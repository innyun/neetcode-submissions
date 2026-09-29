class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        max_length = 0
        m = max(nums)

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            tm = 0
            for i in range(m, n, -1):
                if i in dp:
                    tm = max(tm, dp[i])
            dp[n] = tm + 1
            max_length = max(max_length, dp[n])
            if n not in dp:
                dp[n] = 1
        
        print(dp)
        
        return max_length if max_length > 0 else 1