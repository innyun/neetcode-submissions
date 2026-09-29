class Solution:
    def trap(self, height: List[int]) -> int:
        a, b = 0, len(height) - 1
        area = 0
        prev_a = 0
        prev_b = 0
        while a <= b:
            if prev_a > prev_b:
                if height[b] >= prev_b:
                    prev_b = height[b]
                else:
                    area += prev_b - height[b]
                b -= 1
            else:
                if height[a] >= prev_a:
                    prev_a = height[a]
                else:
                    area += prev_a - height[a]
                a += 1
        return area
        