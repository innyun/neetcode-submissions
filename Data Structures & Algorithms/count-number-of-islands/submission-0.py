class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(i, j):
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '1':
                    grid[ni][nj] = '2'
                    dfs(ni, nj)
        
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] == '1':
                    islands += 1
                    dfs(col, row)

        return islands