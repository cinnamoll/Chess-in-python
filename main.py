import pygame
import engine

pygame.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQR_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImg():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for p in pieces:
        IMAGES[p] = pygame.transform.scale(pygame.image.load("Chess-in-python\\Chess piece\\" + p + ".png"), (SQR_SIZE, SQR_SIZE))
    
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    state = engine.GameState()
    loadImg()

    running = True
    sqSelected = ()
    playerClick = []

    validMoves = state.getValidMoves()
    moveMade = False

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQR_SIZE
                row = location[1] // SQR_SIZE 

                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClick = []
                else:
                    sqSelected = (row, col)
                    playerClick.append(sqSelected)
                
                if len(playerClick) == 2:
                    move = engine.Move(playerClick[0], playerClick[1], state.board)
                    print(move.getChessNotation())
                    
                    if move in validMoves:    
                        state.makeMove(move)
                        moveMade = True
                    sqSelected = ()
                    playerClick = []
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    state.undoMove()
                    moveMade = True

        if moveMade == True:
            validMoves = state.getValidMoves()
            moveMade = False 
        
        drawState(screen, state)
        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQR_SIZE, r*SQR_SIZE, SQR_SIZE, SQR_SIZE))
            

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c] 
            if piece != "--":
               screen.blit(IMAGES[piece], pygame.Rect(c*SQR_SIZE, r*SQR_SIZE, SQR_SIZE, SQR_SIZE)) 


def drawState(screen, state):
    drawBoard(screen)
    drawPieces(screen, state.board)


if __name__ == "__main__":
    main()
