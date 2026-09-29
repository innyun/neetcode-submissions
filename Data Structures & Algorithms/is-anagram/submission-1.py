class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * 26
        for n in s:
            l[ord(n) - ord('a')] += 1
        for n in t:
            l[ord(n) - ord('a')] -= 1
        return all([n == 0 for n in l])