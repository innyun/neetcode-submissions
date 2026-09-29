class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) 
        seen = set()
        m = 0
        for n in nums: 
            if n in seen:
                continue
            seen.add(n)
            t = 1
            cu, cd = n, n
            u, d = True, True
            while u or d:
                if cu + 1 in nums: 
                    cu += 1
                    t += 1
                    seen.add(cu)
                else:
                    u = False
                if cd - 1 in nums:
                    cd -= 1
                    t += 1
                    seen.add(cd)
                else:
                    d = False
            m = max(m, t)

        return m