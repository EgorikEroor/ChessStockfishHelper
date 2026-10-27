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
    'B1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (0 * cellsize, 1 * cellsize)},
    'B2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (1 * cellsize, 1 * cellsize)},
    'B3': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (2 * cellsize, 1 * cellsize)},
    'B4': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (3 * cellsize, 1 * cellsize)},
    'B5': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (4 * cellsize, 1 * cellsize)},
    'B6': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (5 * cellsize, 1 * cellsize)},
    'B7': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (6 * cellsize, 1 * cellsize)},
    'B8': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'B.png')).convert_alpha(), 'Position': (7 * cellsize, 1 * cellsize)},
    'BB1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha(), 'Position': (2 * cellsize, 0)},
    'BB2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BB.png')).convert_alpha(), 'Position': (5 * cellsize, 0)},
    'BK1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BK.png')).convert_alpha(), 'Position': (4 * cellsize, 0)},
    'BN1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha(), 'Position': (1 * cellsize, 0)},
    'BN2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BN.png')).convert_alpha(), 'Position': (6 * cellsize, 0)},
    'BQ1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BQ.png')).convert_alpha(), 'Position': (3 * cellsize, 0)},
    'BR1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha(), 'Position': (0 * cellsize, 0)},
    'BR2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'BR.png')).convert_alpha(), 'Position': (7 * cellsize, 0)},
    'W1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (0 * cellsize, 6 * cellsize)},
    'W2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (1 * cellsize, 6 * cellsize)},
    'W3': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (2 * cellsize, 6 * cellsize)},
    'W4': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (3 * cellsize, 6 * cellsize)},
    'W5': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (4 * cellsize, 6 * cellsize)},
    'W6': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (5 * cellsize, 6 * cellsize)},
    'W7': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (6 * cellsize, 6 * cellsize)},
    'W8': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'W.png')).convert_alpha(), 'Position': (7 * cellsize, 6 * cellsize)},
    'WB1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha(), 'Position': (2 * cellsize, 7 * cellsize)},
    'WB2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WB.png')).convert_alpha(), 'Position': (5 * cellsize, 7 * cellsize)},
    'WK1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WK.png')).convert_alpha(), 'Position': (4 * cellsize, 7 * cellsize)},
    'WN1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha(), 'Position': (1 * cellsize, 7 * cellsize)},
    'WN2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WN.png')).convert_alpha(), 'Position': (6 * cellsize, 7 * cellsize)},
    'WQ1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WQ.png')).convert_alpha(), 'Position': (3 * cellsize, 7 * cellsize)},
    'WR1': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha(), 'Position': (0 * cellsize, 7 * cellsize)},
    'WR2': {'Image': pygame.image.load(str(file_parent / 'Figures' / 'WR.png')).convert_alpha(), 'Position': (7 * cellsize, 7 * cellsize)}
}
chess_figures_rects = {}
chess_board_rects = []
figure_select = None
board_row = '12345678'
board_column = 'abcdefgh'
figure_move = ''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if figure_select:
                    for value in chess_board_rects:
                        if value.collidepoint(event.pos):
                            chess_figures_information[figure_select]['Position'] = (value[:2])
                            figure_select = None
                            figure_move += f'{board_column[int((value[0] / cellsize) - 8)]}{int(abs(value[1] / cellsize - 8))}'
                            figure_move = chess.Move.from_uci(figure_move)
                            if figure_move in chess_board.legal_moves:
                                chess_board.push(figure_move)
                            figure_move = ''
                else:
                    for key,value in chess_figures_rects.items():
                        if value.collidepoint(event.pos):
                            figure_move += f'{board_column[int((value[0] / cellsize) - 8)]}{int(abs(value[1] / cellsize - 8))}'
                            figure_select = key
    chess_board_rects.clear()
    chess_figures_rects.clear()
    screen.fill((255, 255, 255))
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 != 0:
                cellcolor = (140, 201, 54)
            else:
                cellcolor = (255, 242, 212)
            board_element = pygame.draw.rect(screen,cellcolor,(column * cellsize,row * cellsize,cellsize,cellsize))
            chess_board_rects.append(board_element)
    for key, value in chess_figures_information.items():
        screen.blit(value['Image'], (value['Position']))
        chess_figures_rects[key] = value['Image'].get_rect(topleft=(value['Position']))
    pygame.display.flip()
pygame.quit()
sys.exit()