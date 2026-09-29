class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)

        for i in range(amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                if i - coin > 0 and dp[i - coin] < amount + 1:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        
        print(dp)

        return dp[amount] if dp[amount] < amount + 1 else -1


