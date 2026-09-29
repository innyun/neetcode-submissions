class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)
        grid = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[j] == text2[i]:
                    grid[i + 1][j + 1] = grid[i][j] + 1
                else:
                    grid[i + 1][j + 1] = max(grid[i][j], grid[i][j + 1], grid[i + 1][j])

        return grid[m][n]

