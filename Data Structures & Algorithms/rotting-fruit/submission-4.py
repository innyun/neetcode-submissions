class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        minutes = 0
        fresh = 0

        def add(i, j):
            q.append((i, j))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    add(row, col)
                elif grid[row][col] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        add(ni, nj)
            minutes += 1

        return minutes if not fresh else -1

        