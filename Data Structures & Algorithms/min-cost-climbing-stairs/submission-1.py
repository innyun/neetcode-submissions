class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        a, b, = cost[0], cost[1]
        ans = 0
        for i in range(2, len(cost)):
            ans = min(b, a + cost[i])
            a, b = b, min(b + cost[i], a + cost[i])
        return ans