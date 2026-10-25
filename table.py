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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 != 0:
                cellcolor = (140, 201, 54)
            else:
                cellcolor = (255, 242, 212)
            pygame.draw.rect(screen,cellcolor,(column * cellsize,row * cellsize,cellsize,cellsize))
            if row == 0:
                if column in (0, 7):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha()
                elif column in (1, 6):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha()
                elif column in (2, 5):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha()
                elif column == 3:
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'BQ.png')).convert_alpha()
                else:
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'BK.png')).convert_alpha()
                screen.blit(figure_image, (column * cellsize, row * cellsize))
            elif row == 1:
                figure_image = pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha()
                screen.blit(figure_image,(column * cellsize,row * cellsize))
            elif row == 6:
                figure_image = pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha()
                screen.blit(figure_image, (column * cellsize, row * cellsize))
            elif row == 7:
                if column in (0, 7):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha()
                elif column in (1, 6):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha()
                elif column in (2, 5):
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha()
                elif column == 3:
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'WQ.png')).convert_alpha()
                else:
                    figure_image = pygame.image.load(str(file_parent / 'Figures' / 'WK.png')).convert_alpha()
                screen.blit(figure_image, (column * cellsize, row * cellsize))
    pygame.display.flip()
pygame.quit()
sys.exit()