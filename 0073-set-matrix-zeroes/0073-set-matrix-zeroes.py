class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        row = False
        col = False

        # Check if first row has a zero
        for j in range(n):
            if matrix[0][j] == 0:
                row = True
                break

        # Check if first column has a zero
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Zero first row
        if row:
            for j in range(n):
                matrix[0][j] = 0

        # Zero first column
        if col:
            for i in range(m):
                matrix[i][0] = 0