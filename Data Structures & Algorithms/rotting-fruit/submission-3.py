class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        minutes = 0

        def add(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                q.append((i, j))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    add(row, col + 1)
                    add(row + 1, col)
                    add(row - 1, col)
                    add(row, col - 1)
        
        while q:
            print(grid, q)
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = 2
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni, nj))
            minutes += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return minutes

        