import CalcMove
import PieceMove

class GameState():
    def __init__(self):
        self.board = CalcMove.Move.board
        self.whiteToPlay = True
        self.moveLog = []
        self.moveFunc = {'p': PieceMove.getPawnMoves, 'R': PieceMove.getRookMoves, 'N': PieceMove.getKnightMoves,
                         'B': PieceMove.getBishopMoves, 'Q': PieceMove.getQueenMoves, 'K': PieceMove.getKingMoves}
        
        self.blackKingLocation = (0, 4)
        self.whiteKingLocation = (7, 4)

        if CalcMove.Move.pieceMoved == 'wK':
            self.whiteKingLocation = (CalcMove.Move.endRow, CalcMove.Move.endCol)

        if CalcMove.Move.pieceMoved == 'bK':
            self.blackKingLocation = (CalcMove.Move.endRow, CalcMove.Move.endCol)

        self.checkmate = False
        self.stalemate = False 

    
    def makeMove(self, move):
        CalcMove.Move.board[move.startRow][move.startCol] = "--"
        CalcMove.Move.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToPlay = not self.whiteToPlay

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            CalcMove.Move.board[move.startRow][move.startCol] = move.pieceMoved
            CalcMove.Move.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToPlay = not self.whiteToPlay

    def getValidMoves(self):
        moves = self.getAllMoves()
        for i in range(len(moves) - 1, -1, -1):
            self.makeMove(moves[i])
            oppMoves = self.getAllMoves()
            self.whiteToPlay = not self.whiteToPlay
            if self.inChecks():
                moves.remove(moves[i])
            self.whiteToPlay = not self.whiteToPlay
            self.undoMove()

        if len(moves) == 0:
            if self.inChecks():
                self.checkmate = True
            else:
                self.stalemate = True
        else:
            self.checkmate = False
            self.stalemate = False
        return moves

    def getAllMoves(self):
        moves = []
        for r in range(len(CalcMove.Move.board)):
            for c in range(len(CalcMove.Move.board[r])):
                turn = CalcMove.Move.board[r][c][0]
                if (turn == 'w' and self.whiteToPlay) or (turn == 'b' and not self.whiteToPlay):
                    piece = CalcMove.Move.board[r][c][1]
                    self.moveFunc[piece](r, c, moves, whiteToPlay=self.whiteToPlay, board=CalcMove.Move.board)
        return moves
    
    def inChecks(self):
        if self.whiteToPlay:
            return self.squareInAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareInAttack(self.blackKingLocation[0], self.blackKingLocation[1])

    def squareInAttack(self, r, c):
        self.whiteToPlay = not self.whiteToPlay
        oppMoves = self.getAllMoves()
        self.whiteToPlay = not self.whiteToPlay

        for moves in oppMoves:
            if CalcMove.Move.endRow == r and CalcMove.Move.endCol == c:
                return True
        
        return False