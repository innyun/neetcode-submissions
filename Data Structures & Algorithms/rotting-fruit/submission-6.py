class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        directions = ([0, 1], [0, -1], [1, 0], [-1, 0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr, nc])
            minutes += 1

        return -1 if fresh > 0 else minutes
        
        