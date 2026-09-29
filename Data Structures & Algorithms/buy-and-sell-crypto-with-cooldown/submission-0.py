class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buy, value):
            if i >= len(prices):
                print(i, buy, value)
                return value
            if buy:
                return max(dfs(i + 1, False, value - prices[i]), dfs(i + 1, True, value))
            else:
                return max(dfs(i + 2, True, value + prices[i]), dfs(i + 1, False, value))
        
        return dfs(0, True, 0)
            
            
