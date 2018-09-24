class Solution:
    def __init__(self):
        self.board = None
    def validate_board(self, r, c, w):
        for i in range(w):
            u1 = dict()   
            u2 = dict()
            for j in range(w):
                if self.board[i][j] == '.' or self.board[i][j] not in u1:
                    u1[self.board[i][j]] = True
                else:
                    return False
                if self.board[j][i] == '.' or self.board[j][i] not in u2:
                    u2[self.board[j][i]] = True
                else:
                    return False
        
        for i in range(9):
            u = dict()
            c0 = i % 3 * 3
            r0 = i // 3 * 3
            for j in range(9):
                
                r = j //3 + r0 
                c = j % 3 + c0
                if self.board[r][c] == '.' or self.board[r][c] not in u:
                    u[self.board[r][c]] = True
                else:
                    return False
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for i in board:
            print(i)
        return self.validate_board(0,0,9)