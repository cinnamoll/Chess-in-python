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
        IMAGES[p] = pygame.transform.scale(pygame.image.load("Chess-in-python\Chess piece\\" + p + ".png"), (SQR_SIZE, SQR_SIZE))
    
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    state = engine.GameState()
    loadImg()

    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        clock.tick(MAX_FPS)
        pygame.display.flip()


def drawBoard(screen):
    colors = [pygame.color("white"), pygame.color("brown")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.rect(c*SQR_SIZE, r*SQR_SIZE, SQR_SIZE, SQR_SIZE))
            

def drawPieces(screen, board):
    pass

def drawState(screen, state):
    drawBoard(screen)
    drawPieces(screen, state.board)


if __name__ == "__main__":
    main()



#"C:\Code\chess\Chess-in-python\Chess piece\bp.png"