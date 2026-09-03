class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for y in range(rows):
            for x in range(cols):
                count = 0

                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx

                    if 0 <= ny < rows and 0 <= nx < cols:
                        if board[ny][nx] in (1, 3):
                            count += 1

                if board[y][x] == 1:
                    if count < 2 or count > 3:
                        board[y][x] = 3
                else:
                    if count == 3:
                        board[y][x] = 2
                        
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == 2:
                    board[y][x] = 1
                elif board[y][x] == 3:
                    board[y][x] = 0
