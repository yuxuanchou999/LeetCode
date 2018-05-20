class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(board, x, y):
            for i in range(len(board)):
                if i != x and board[x][y] == board[i][y]:
                    return False
            for j in range(len(board[0])):
                if j != y and board[x][y] == board[x][j]:
                    return False   
            i = 3 * (x // 3)
            while i < 3 * (x // 3 + 1):
                j = 3 * (y // 3)
                while j < 3 * (y // 3 + 1):
                    if (i != x or j != y) and board[x][y] == board[i][j]:
                        return False
                    j += 1
                i += 1
            return True
        
        def solver(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        for k in range(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
                
        solver(board)
