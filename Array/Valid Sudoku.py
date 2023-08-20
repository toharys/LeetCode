class Solution(object):
    
    def checkRows(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if len(row)!=9:
                return False
            flag={}
            for cell in row:
                # print(cell+' '+flag[cell]+'\n')
                if cell in flag and cell!=".":
                    return False
                flag[cell]=1
        return True
                
    def checkCols(self, board):
        for j in range(9):
            flag={}
            for i in range(9):
                if board[i][j] in flag and board[i][j]!=".":
                    return False
                flag[board[i][j]]=1
        return True
    
    def checkBoxes(self, board):
        for i in range(3):
            for t in range(3):
                flag={}
                for j in range(3):
                    for k in range(3):
                        if board[3*i+j][3*t+k] in flag and board[3*i+j][3*t+k]!=".":
                            return False
                        flag[board[3*i+j][3*t+k]]=1
        return True
                
        
    def isValidSudoku(self, board):
        if not board or len(board)!=9:
            return False
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)         
