class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        low = float('inf')
        c = 0
        while c < len(prices):
            low = min(prices[c], low)
            maxP = max(prices[c] - low, maxP)
            c += 1
        return maxP
