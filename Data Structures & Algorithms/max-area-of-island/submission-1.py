class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            temp_area = 1

            while q:
                row, col = q.popleft()
                for direction in directions:
                    ni, nj = row + direction[0], col + direction[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        temp_area += 1
                        grid[ni][nj] = 2
                        q.append((ni, nj))
                

            return temp_area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    m = max(m, bfs(row, col))

        return m