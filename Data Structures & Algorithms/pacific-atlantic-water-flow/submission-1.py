class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
                
        def dfs(i, j, s):
            s.add((i, j))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < rows and 0 <= nj < cols and heights[i][j] <= heights[ni][nj] and (ni, nj) not in s:
                    dfs(ni, nj, s)
                    
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)
        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows-1, j, atlantic)

        both = []

        for pair in pacific:
            if pair in atlantic:
                both.append(pair)

        return both
        
