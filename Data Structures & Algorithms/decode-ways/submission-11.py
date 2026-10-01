class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1 if s[0] > '0' else 0
            
        dp = [0] * len(s) 
        dp[0] = 1

        if s[0] == '0':
            return 0
        if '10' <= s[:2] <= '26' and s[1] > '0':
            dp[1] = 1 + dp[0]
        elif s[:2] >= '30' and s[1] == '0':
            return 0 
        else:
            dp[1] = dp[0]

        for i in range(2, len(s)):
            if s[i] > '0':
                dp[i] += dp[i - 1]
            if '10' <= s[i - 1:i + 1] <= '26':
                dp[i] += dp[i - 2]
        return dp[len(s) - 1]
        