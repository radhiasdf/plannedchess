import chess
import pygame as pg
from assets import pieceImgs


def scaleImages(scale):  # Vector2 scale  # returns dict
	pieceTransforms = {}
	for key in pieceImgs.keys():
		pieceTransforms[key] = pg.transform.scale(pieceImgs[key], scale)
	return pieceTransforms


def coordToPixel(coord):
	return coord[0] * square_size[0], coord[1] * square_size[1]


def draw_piece(piece_key, coord):
	if board.piece_at(row * 8 + col) is None:
		return
	try:
		dest = coordToPixel(coord)
		screen.blit(pieceTransforms[str(piece_key)], dest)
	except KeyError:
		pass


screen_dim = pg.Vector2(600,600)
square_size = screen_dim/8

# create board object
board = chess.Board()

# display chess board in terminal
print(board)

background_colour = (234, 212, 252)
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Geeksforgeeks')
pg.display.flip()

pieceTransforms = scaleImages(square_size)
print(pieceTransforms)

# Variable to keep our game loop running
running = True

# game loop
while running:
	screen.fill(background_colour)
	for row in range(8):
		for col in range(8):
			if (row+col+1) % 2 == 0:
				pg.draw.rect(screen, "white", (row*square_size.x, col*square_size.y, square_size.x, square_size.y))
			try:
				draw_piece(str(board.piece_at(row*8+col)), (col, row))
			except:
				pass
	pg.display.update()

	# for loop through the event queue
	for event in pg.event.get():

		# Check for QUIT event
		if event.type == pg.QUIT:
			running = False

