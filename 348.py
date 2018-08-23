class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [['#' for _ in range(n)] for _ in range(n)]
        self.dic = {1:0, 2:0}
        self.n = len(self.board)

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.dic[player] += 1
        self.board[row][col] = 'X' if player == 1 else 'O'
        if self.dic[player] < self.n: return 0
        if self.board[row] == ['X'] * self.n or self.board[row] == ['O'] * self.n: return player #row
        if row == col:
            i = 0
            while i < self.n:
                if self.board[i][i] != self.board[row][col]: break
                i += 1
            if i == self.n: return player
        if row + col == self.n - 1:
            i = 0
            while i < self.n:
                if self.board[i][self.n - i - 1] != self.board[row][col]: break #diagonal
                i += 1
            if i == self.n: return player
        i = 0
        while i < self.n:
            if self.board[i][col] != self.board[row][col]: break           #col
            i += 1
        if i == self.n: return player
        return 0
        
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
