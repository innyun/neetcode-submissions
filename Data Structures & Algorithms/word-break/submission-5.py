class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(dp) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp) and s[i: i + len(word)] in wordDict:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]

        