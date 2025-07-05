import CalcMove
import PieceMove

class GameState():
    def __init__(self):
        self.board = CalcMove.Move.board
        self.whiteToPlay = True
        self.moveLog = []
        self.moveFunc = {'p': PieceMove.getPawnMoves, 'R': PieceMove.getRookMoves, 'N': PieceMove.getKnightMoves,
                         'B': PieceMove.getBishopMoves, 'Q': PieceMove.getQueenMoves, 'K': PieceMove.getKingMoves}

    
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
        return self.getAllMoves()

    def getAllMoves(self):
        moves = []
        for r in range(len(CalcMove.Move.board)):
            for c in range(len(CalcMove.Move.board[r])):
                turn = CalcMove.Move.board[r][c][0]
                if (turn == 'w' and self.whiteToPlay) or (turn == 'b' and not self.whiteToPlay):
                    piece = CalcMove.Move.board[r][c][1]
                    self.moveFunc[piece](r, c, moves, whiteToPlay=self.whiteToPlay, board=CalcMove.Move.board)
        return moves