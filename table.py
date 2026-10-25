import sys
import pygame
import chess
import chess.engine
from pathlib import Path

tablesize = 576
cellsize = 72
cellcolor = ()
running = True
stockfish_path = str(
    Path(__file__).parent.resolve() / "stockfish-windows-x86-64-universal.exe"
)
chess_engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
chess_board = chess.Board()
print(Path(__file__).parent.resolve() )
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
    pygame.display.flip()
pygame.quit()
sys.exit()