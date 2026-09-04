class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        direction = [-1, 1 , 0]
        coordinate = []
        for d in direction:
            for d2 in direction:
                coordinate.append([d , d2])
        
        coordinate.pop()

        def legal(nx, ny):
            if nx < 0 or ny < 0:
                return False
            if nx >= len(board):
                return False
            if ny >= len(board[0]):
                return False
            
            return True
        
        for idxr,r in enumerate(board):
            for idxc, c in enumerate(r):
                count = 0
                for d in coordinate:
                    nx = d[0] + idxr 
                    ny =  d[1] + idxc

                    if legal(nx,ny) and board[nx][ny] in [1, 3]:
                        count += 1
                if c == 0:
                    if count == 3:
                        board[idxr][idxc] = 2
                else:
                    if count < 2 or count > 3:
                        board[idxr][idxc] = 3
        
        for idxr,r in enumerate(board):
            for idxc, c in enumerate(r):
                if c == 3:
                    board[idxr][idxc] = 0
                elif c == 2:
                    board[idxr][idxc] = 1

        