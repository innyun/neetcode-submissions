class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = ([-1, 0], [1, 0], [0, 1], [0, -1])
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "-1":
                    continue
                elif grid[r][c] == "1":
                    islands += 1
                    q = deque([[r, c]])
                    while q:
                        tr, tc = q.popleft()
                        for d in directions:
                            nr, nc = tr + d[0], tc + d[1]
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                q.append([nr, nc])
                                grid[nr][nc] = "-1"
                grid[r][c] = "-1"
                    

        return islands