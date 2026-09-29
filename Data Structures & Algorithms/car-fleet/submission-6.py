class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        times = list(zip(position, speed))
        times.sort(reverse=True)
        for p, s in times:
            t = (target - p) / s
            if st and st[-1] >= t:
                continue
            else:
                st.append(t)
        return len(st)