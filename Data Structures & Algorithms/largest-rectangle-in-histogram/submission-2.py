class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        for i, h in enumerate(heights):
            if st and h <= st[-1][0]:
                sh, si = st.pop()
                while sh > h:
                    max_area = max(sh * (i - si), max_area)
                    if st and st[-1][0] > h:
                        sh, si = st.pop()
                    else:
                        break
                st.append((h, si))
            else:
                st.append((h, i))
        while st:       
            h, i = st.pop()
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
