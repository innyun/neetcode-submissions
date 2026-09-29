class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        lb, rb, tb, db = -1, n, -1, m
        x = 0

        i = 0
        j = 0

        elements = [matrix[0][0]]

        while len(elements) != m * n:
            di = x % 4
            d = direction[di]
            ni, nj = i + d[0], j + d[1]
            if tb < ni < db and lb < nj < rb:
                elements.append(matrix[ni][nj])
                i = ni
                j = nj
            else:
                x += 1
                if di == 0:
                    tb += 1
                if di == 1:
                    rb -= 1
                if di == 2:
                    db -= 1
                if di == 3:
                    lb += 1

        return elements

