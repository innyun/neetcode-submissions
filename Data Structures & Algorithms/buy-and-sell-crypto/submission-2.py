class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        low = prices[0]
        for c in prices:
            low = min(c, low)
            maxP = max(c - low, maxP)
        return maxP
