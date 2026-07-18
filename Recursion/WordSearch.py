class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)

        n , m = len(board) , len(board[0])
        
        def checking(x,y):
            if(x <= -1 or x >= n or y <= -1 or y >= m):
                return False
            return True
        
        def solution():
            for x in range(n):
                for y in range(m):
                    original = board[x][y]
                    print(original)
                    if(board[x][y] == word[0]):
                        board[x][y] = "*"
                        response = finder(1 , x , y)
                        if(response):
                            return True
                        board[x][y] = original
            
            return False
        

        def finder(anslen , x , y):
            if(anslen == word_len):
                return True
            
            for i in [[0,1] , [0,-1] ,[1, 0], [-1,0]]:
                xi , yi = x + i[0] , y + i[1]
                if(checking(xi , yi)):
                    original = board[xi][yi]
                    # print(original , xi , yi)
                    if(word[anslen] == board[xi][yi]):
                        board[xi][yi] = "*"
                        if(finder(anslen + 1 , xi , yi)):
                            return True
                        board[xi][yi] = original
            
            return False

        return solution()