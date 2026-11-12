class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        out = ""
        for i in range(min(l1, l2)):
            out += word1[i]
            out += word2[i]
        out += word1[i+1:]
        out += word2[i+1:]

        return out