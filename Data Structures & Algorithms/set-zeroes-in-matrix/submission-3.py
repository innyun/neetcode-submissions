class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = True, True

        if matrix[0][0] == 0:
            row, col = False, False
        if any(matrix[0][i] == 0 for i in range(1, len(matrix[0]))):
            row = False
        if any(matrix[i][0] == 0 for i in range(1, len(matrix))):
            col = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        if not row:
            for i in range(1, len(matrix[0])):
                matrix[0][i] = 0
        if not col:
            for i in range(1, len(matrix)):
                matrix[i][0] = 0

        

