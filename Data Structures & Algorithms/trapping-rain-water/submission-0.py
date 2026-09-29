class Solution:
    def trap(self, height: List[int]) -> int:
        a, b = 0, len(height) - 1
        area = 0
        prev_a = 0
        prev_b = 0
        temp_a = 0
        temp_b = 0
        while a < b:
            if height[a] > height[b]:
                if height[b] >= prev_b:
                    area += temp_b
                    temp_b = 0
                    prev_b = height[b]
                else:
                    temp_b += prev_b - height[b]
                b -= 1
            else:
                if height[a] >= prev_a:
                    area += temp_a
                    temp_a = 0
                    prev_a = height[a]
                else:
                    temp_a += prev_a - height[a]
                a += 1
        area += temp_a + temp_b
        return area
        