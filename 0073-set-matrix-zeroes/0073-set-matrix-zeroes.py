class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def makeZero(i , j):
            for x in range(len(matrix)):
                if(matrix[x][j] == 0):
                    continue
                matrix[x][j] = "x"
                
            for y in range(len(matrix[i])):
                if(matrix[i][y] == 0):
                    continue
                matrix[i][y] = "x"


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(i , j , matrix[i][j])
                if(matrix[i][j] == 0):
                    makeZero(i , j)
                    
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == "x"):
                    matrix[i][j] = 0
        

        