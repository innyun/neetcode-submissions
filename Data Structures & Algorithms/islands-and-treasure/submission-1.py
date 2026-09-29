class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        distance = 1

        def add_source(i, j):
            q.append((i, j))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    add_source(row, col)            

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] > distance:
                        grid[ni][nj] = distance
                        q.append((ni, nj)) 
            distance += 1
