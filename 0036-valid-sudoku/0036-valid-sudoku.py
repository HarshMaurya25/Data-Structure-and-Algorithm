class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if(board[i][j] == "."):
                    continue
                temp = board[i][j]
                board[i][j] = "."
                if(self.checking(board , i , j , temp) is False):
                    return False
                board[i][j] = temp
        return True


    def checking(self, board, x, y, num):
        for i in range(9):
            row = (x // 3) * 3 + i // 3
            col = (y // 3) * 3 + i % 3

            if (
                board[i][y] == num or
            board[x][i] == num or
            board[row][col] == num
        ):
                return False

        return True