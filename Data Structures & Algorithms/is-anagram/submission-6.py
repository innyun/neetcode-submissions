class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sd, td = defaultdict(int), defaultdict(int)

        for v in s:
            sd[v] += 1
        
        for v in t:
            td[v] += 1

        return sd == td