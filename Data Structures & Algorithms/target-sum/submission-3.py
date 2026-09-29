class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = (sum(nums) + target)
        if t % 2 == 1:
            return 0
        
        t //= 2

        dp = [[0] * (t + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(0, t + 1):   # include j = 0
                # don't take
                dp[i][j] = dp[i - 1][j]
                
                # take (if possible)
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]

        print(dp)

        return dp[len(nums)][t]
