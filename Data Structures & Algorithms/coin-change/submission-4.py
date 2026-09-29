class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                if i - coin > 0 and dp[i - coin] < amount + 1:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1