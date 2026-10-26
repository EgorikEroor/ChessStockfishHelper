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

chess_figures_image = {
    'B': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(),
    'BB': pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha(),
    'BK': pygame.image.load(str(file_parent / 'Figures' / 'BK.png')).convert_alpha(),
    'BN': pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha(),
    'BQ': pygame.image.load(str(file_parent / 'Figures' / 'BQ.png')).convert_alpha(),
    'BR': pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha(),
    'W': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(),
    'WB': pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha(),
    'WK': pygame.image.load(str(file_parent / 'Figures' / 'WK.png')).convert_alpha(),
    'WN': pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha(),
    'WQ': pygame.image.load(str(file_parent / 'Figures' / 'WQ.png')).convert_alpha(),
    'WR': pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha()
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
            chess_figure_key = ''
            if row == 0:
                if column in (0, 7):
                    chess_figure_key = 'BR'
                elif column in (1, 6):
                    chess_figure_key = 'BN'
                elif column in (2, 5):
                    chess_figure_key = 'BB'
                elif column == 3:
                    chess_figure_key = 'BQ'
                else:
                    chess_figure_key = 'BK'
            elif row == 1:
                chess_figure_key = 'B'
            elif row == 6:
                chess_figure_key = 'W'
            elif row == 7:
                if column in (0, 7):
                    chess_figure_key = 'WR'
                elif column in (1, 6):
                    chess_figure_key = 'WN'
                elif column in (2, 5):
                    chess_figure_key = 'WB'
                elif column == 3:
                    chess_figure_key = 'WQ'
                else:
                    chess_figure_key = 'WK'
            if chess_figure_key:
                screen.blit(chess_figures_image[chess_figure_key], (column * cellsize, row * cellsize))
                chess_figures_rects[chess_figure_key] = chess_figures_image[chess_figure_key].get_rect(topleft=(column * cellsize, row * cellsize))
    pygame.display.flip()
pygame.quit()
sys.exit()