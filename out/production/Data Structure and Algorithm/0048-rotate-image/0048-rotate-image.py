class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        i = 0
        j = n - 1
        while i < j:
            for k in range(n):
                matrix[k][j] , matrix[k][i] = matrix[k][i], matrix[k][j]
            
            i += 1
            j -= 1
        