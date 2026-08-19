class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [0 for i in range(n)]
        solutions = []
        count = 0

        def checking(x , y):
            for i in range(y):
                if(board[i] == x):
                    return False
            for i in range(y):
                if(abs(board[i] - x) == abs(y - i)):
                    return False
            return True
        
        def solution(y):
            global count
            if(y >= n):
                return 1
            ans = 0
            for i in range(n):
                if(checking(i , y)):
                    board[y] = i
                    ans += solution(y + 1)
                    board[y] = -1
            
            return ans

        count = solution(0)

        return count