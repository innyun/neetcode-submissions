class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def recurse(s, i, w):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            j = i
            while j <= len(s):
                if s[i:j] in w and recurse(s, j, w):
                    memo[i] = True
                    return True
                j += 1
            
            memo[i] = False
            return False

        return recurse(s, 0, wordDict)