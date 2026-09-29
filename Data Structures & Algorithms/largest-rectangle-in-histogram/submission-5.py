class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        for i, h in enumerate(heights):
            if st and h <= st[-1][0]:
                si = i
                while st and st[-1][0] > h:
                    sh, si = st.pop()
                    max_area = max(sh * (i - si), max_area)
                st.append((h, si))
            else:
                st.append((h, i))
        while st:       
            h, i = st.pop()
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
