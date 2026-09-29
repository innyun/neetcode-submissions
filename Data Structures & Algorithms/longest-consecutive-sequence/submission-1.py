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
            c = n
            while True:
                if c - 1 in nums:
                    seen.add(c - 1)
                    t += 1
                    c -= 1
                else:
                    break
            c = n
            while True:
                if c + 1 in nums:
                    seen.add(c + 1)
                    t += 1
                    c += 1
                else:
                    break
            m = max(m, t)

        return m