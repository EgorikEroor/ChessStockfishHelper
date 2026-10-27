import sys
import pygame
import chess
import chess.engine
from pathlib import Path

tablesize = 576
cellsize = 72
cellcolor = ()
running = True
file_parent = Path(__file__).parent.resolve()
stockfish_path = str(file_parent
     / "stockfish-windows-x86-64-universal.exe"
)
chess_engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
chess_board = chess.Board()
pygame.init()


screen = pygame.display.set_mode((tablesize,tablesize))
pygame.display.set_caption('ChessStockfishHelper')

chess_figures_information = {
    'B1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 0 * cellsize)},
    'B2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 1 * cellsize)},
    'B3': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 2 * cellsize)},
    'B4': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 3 * cellsize)},
    'B5': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 4 * cellsize)},
    'B6': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 5 * cellsize)},
    'B7': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 6 * cellsize)},
    'B8': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 7 * cellsize)},
    'BB1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha(), 'Position': (0, 2 * cellsize)},
    'BB2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha(), 'Position': (0, 5 * cellsize)},
    'BK1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BK.png')).convert_alpha(), 'Position': (0, 4 * cellsize)},
    'BN1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha(), 'Position': (0, 1 * cellsize)},
    'BN2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha(), 'Position': (0, 6 * cellsize)},
    'BQ1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BQ.png')).convert_alpha(), 'Position': (0, 3 * cellsize)},
    'BR1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha(), 'Position': (0, 0 * cellsize)},
    'BR2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha(), 'Position': (0, 7 * cellsize)},
    'W1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 0 * cellsize)},
    'W2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 1 * cellsize)},
    'W3': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 2 * cellsize)},
    'W4': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 3 * cellsize)},
    'W5': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 4 * cellsize)},
    'W6': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 5 * cellsize)},
    'W7': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 6 * cellsize)},
    'W8': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 7 * cellsize)},
    'WB1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha(), 'Position': (7 * cellsize, 2 * cellsize)},
    'WB2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha(), 'Position': (7 * cellsize, 5 * cellsize)},
    'WK1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WK.png')).convert_alpha(), 'Position': (7 * cellsize, 4 * cellsize)},
    'WN1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha(), 'Position': (7 * cellsize, 1 * cellsize)},
    'WN2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha(), 'Position': (7 * cellsize, 6 * cellsize)},
    'WQ1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WQ.png')).convert_alpha(), 'Position': (7 * cellsize, 3 * cellsize)},
    'WR1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha(), 'Position': (7 * cellsize, 0 * cellsize)},
    'WR2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha(), 'Position': (7 * cellsize, 7 * cellsize)}
}
chess_figures_rects = {}


figure_image = None
figure_rect = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for key,value in chess_figures_rects.items():
                    if value.collidepoint(event.pos):
                        pass
    screen.fill((255, 255, 255))
    chess_figures_rects.clear()
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 != 0:
                cellcolor = (140, 201, 54)
            else:
                cellcolor = (255, 242, 212)
            pygame.draw.rect(screen,cellcolor,(column * cellsize,row * cellsize,cellsize,cellsize))
            for key, value in chess_figures_information.items():
                if value['Position'] == (row * cellsize, column * cellsize):
                    screen.blit(value['Image'], (column * cellsize, row * cellsize))
                    chess_figures_rects[key] = value['Image'].get_rect(topleft=(column * cellsize, row * cellsize))
    pygame.display.flip()
pygame.quit()
sys.exit()