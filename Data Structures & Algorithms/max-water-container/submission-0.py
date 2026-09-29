class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        a, b = 0, len(heights) - 1
        while a < b:
            m = max(m, min(heights[a], heights[b]) * (b - a))
            if heights[b] > heights[a]:
                a += 1
            else:
                b -= 1 
        return m
