import CalcMove

whiteToPlay = True

def getPawnMoves(r, c, moves, whiteToPlay, board):
    if whiteToPlay:
        if board[r-1][c] == '--':
            moves.append(CalcMove.Move((r, c), (r-1, c), board))

            if r == 6 and board[r-2][c] == '--':
                moves.append(CalcMove.Move((r, c), (r-2, c), board))

        if c - 1 >= 0:
            if board[r-1][c-1][0] == 'b':
                moves.append(CalcMove.Move((r, c), (r-1, c-1), board))

        if c + 1 <= 7:
            if board[r-1][c+1][0] == 'b':
                moves.append(CalcMove.Move((r, c), (r-1, c+1), board))
    else:
        if board[r+1][c] == '--':
            moves.append(CalcMove.Move((r, c), (r+1, c), board))

            if r == 1 and board[r+2][c] == '--':
                moves.append(CalcMove.Move((r, c), (r+2, c), board))

        if c - 1 >= 0:
            if board[r+1][c-1][0] == 'w':
                moves.append(CalcMove.Move((r, c), (r+1, c-1), board))

        if c + 1 <= 7:
            if board[r+1][c+1][0] == 'w':
                moves.append(CalcMove.Move((r, c), (r+1, c+1), board))

def helperFunc(r, c, moves, whiteToPlay, board, directions):
    temp = 1 if whiteToPlay else 0

    for dr, dc in directions:
        r_cur, c_cur = r + dr, c + dc
        while 0 <= r_cur <= 7 and 0 <= c_cur <= 7:
            color = board[r_cur][c_cur][0]
            if temp == 1:
                if color == 'w':
                    break
                elif color == 'b':
                    moves.append(CalcMove.Move((r, c), (r_cur, c_cur), board))
            else:
                if color == 'b':
                    break
                elif color == 'w':
                    moves.append(CalcMove.Move((r, c), (r_cur, c_cur), board))
                    
            moves.append(CalcMove.Move((r, c), (r_cur, c_cur), board))
            r_cur += dr
            c_cur += dc

def getRookMoves(r, c, moves, whiteToPlay, board):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    helperFunc(r, c, moves, whiteToPlay, board, directions)

def getKnightMoves(r, c, moves, whiteToPlay, board):
    pass

def getBishopMoves(r, c, moves, whiteToPlay, board):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    helperFunc(r, c, moves, whiteToPlay, board, directions)

def getQueenMoves(r, c, moves, whiteToPlay, board):
    getRookMoves(r, c, moves, whiteToPlay, board)
    getBishopMoves(r, c, moves, whiteToPlay, board)

def getKingMoves(r, c, moves, whiteToPlay, board):
    pass
