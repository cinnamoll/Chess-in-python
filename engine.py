class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "wR", "--", "--", "bR", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.moveFunc = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                         'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}

        self.whiteToPlay = True
        self.moveLog = []

    # def check(self):
    #     return self.whiteToPlay
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToPlay = not self.whiteToPlay
   
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToPlay = not self.whiteToPlay

    def getValidMoves(self):
        return self.getAllMoves()

    def getAllMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToPlay) or (turn == 'b' and not self.whiteToPlay):
                    piece = self.board[r][c][1]
                    self.moveFunc[piece](r, c, moves)
        return moves

    def getPawnMoves(self, r, c, moves):
        if self.whiteToPlay:
            if self.board[r-1][c] == '--':
                moves.append(Move((r, c), (r-1, c), self.board))

                if r == 6 and self.board[r-2][c] == '--':
                    moves.append(Move((r,c), (r-2, c), self.board))

            if c - 1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r, c), (r-1, c-1), self.board))
            
            if c + 1 <= 7:
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r, c), (r-1, c+1), self.board))
        else:
            if self.board[r+1][c] == '--':
                moves.append(Move((r, c), (r+1, c), self.board))

                if r == 1 and self.board[r+2][c] == '--':
                    moves.append(Move((r,c), (r+2, c), self.board))

            if c - 1 >= 0:
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(Move((r, c), (r+1, c-1), self.board))
            
            if c + 1 <= 7:
                if self.board[r+1][c+1][0] == 'w':
                    moves.append(Move((r, c), (r+1, c+1), self.board))


    def getRookMoves(self, r, c, moves):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        temp = 1 if self.whiteToPlay else 0

        for dr, dc in directions:
            r_cur, c_cur = r + dr, c + dc
            while 0 <= r_cur <= 7 and 0 <= c_cur <= 7:
                color = self.board[r_cur][c_cur][0]
                if temp == 1:
                    if color == 'w':
                        break
                    elif color == 'b':
                        moves.append(Move((r,c), (r_cur, c_cur), self.board))
                        break
                else:
                    if color == 'b':
                        break
                    elif color == 'w':
                        moves.append(Move((r,c), (r_cur, c_cur), self.board))
                        break
                moves.append(Move((r, c), (r_cur, c_cur), self.board))
                    
                r_cur += dr
                c_cur += dc
        

    def getKnightMoves(self, r, c, moves):
        pass

    def getBishopMoves(self, r, c, moves):
        pass

    def getQueenMoves(self, r, c, moves):
        pass

    def getKingMoves(self, r, c, moves):
        pass


class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k,v in filesToCols.items()}

    def __init__(self, startSqr, endSqr, board):
        self.startRow = startSqr[0]
        self.startCol = startSqr[1]
        
        self.endRow = endSqr[0]
        self.endCol = endSqr[1]

        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

        self.id = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.id == other.id
        return False

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)