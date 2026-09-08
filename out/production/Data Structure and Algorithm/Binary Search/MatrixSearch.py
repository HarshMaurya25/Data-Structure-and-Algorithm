class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def column(low  , high):
            mid = low + (high - low)//2

            if(low > high):
                return False

            length = len(matrix[mid]) - 1

            if(matrix[mid][0] <= target <= matrix[mid][length]):
                return row(mid , 0 , length)
            elif(matrix[mid][0] > target):
                return column(low , mid - 1)
            else:
                return column(mid + 1, high)
        
        def row(col , low , high):
            mid = low + (high - low)//2

            # print(f"Row : [{low} , {high}] Matrix : ", matrix[col][mid])
            if(low > high):
                return False

            if(matrix[col][mid] == target):
                return True
            elif(matrix[col][mid] > target):
                return row(col , low , mid - 1)
            else:
                return row(col , mid + 1 , high)

        return column(0 , len(matrix) - 1)