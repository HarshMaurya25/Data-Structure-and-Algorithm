class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [0 for i in range(n)]
        solutions = []

        def checking(x , y):
            for i in range(y):
                if(board[i] == x):
                    return False
            for i in range(y):
                if(abs(board[i] - x) == abs(y - i)):
                    return False
            return True
        
        def solution(y):
            if(y >= n):
                print("T")
                board_printing()
                return 1
            
            for i in range(n):
                if(checking(i , y)):
                    board[y] = i
                    solution(y + 1)
                    board[y] = -1

        def board_printing():
            board_current = []
            for i in range(n):
                current = []
                for j in range(n):
                    current.append(".")
                current[board[i]] = "Q"
                board_current.append("".join(current))
            solutions.append(board_current)
            print(board_current)

        solution(0)

        return solutions
