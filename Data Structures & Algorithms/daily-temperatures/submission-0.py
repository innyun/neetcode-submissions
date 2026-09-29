class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        out = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                _, j = st.pop()
                out[j] = i - j
            st.append((t, i))
                  
        return out;