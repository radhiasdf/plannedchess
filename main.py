import chess
import pygame as pg
from assets import pieceImgs

pg.init()
font = pg.font.Font(None, 36)

def scaleImages(scale):  # Vector2 scale  # returns dict
	pieceTransforms = {}
	for key in pieceImgs.keys():
		pieceTransforms[key] = pg.transform.scale(pieceImgs[key], scale)
	return pieceTransforms


def coordToPixel(coord):
	return int(coord[0] * square_size[0]), int(coord[1] * square_size[1])


def draw_piece(piece_key, coord):
	if str(piece_key) == "None":
		print("it will return")
	try:
		print(str(piece_key))
		print(coordToPixel(coord))
		screen.blit(pieceTransforms[str(piece_key)], coordToPixel(coord))
	except KeyError:
		print("keyerror")
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
	for row in range(0,8):
		for col in range(0, 8):
			if (row+col) % 2 == 0:
				pg.draw.rect(screen, "white", (row*square_size.x, col*square_size.y, square_size.x, square_size.y))
	for row in range(0,8):
		for col in range(0, 8):
			draw_piece(str(board.piece_at(63-(row*8+col))), (col, row))
			print(63-(row*8+col))
			print(col, row)


	text_surface = font.render(str(pg.mouse.get_pos()), True, (0, 0, 0))  # Text, antialias, color
	text_rect = text_surface.get_rect()
	text_rect.center = (screen_dim // 2)  # Center the text

	# Blit the text onto the screen
	screen.blit(text_surface, text_rect)

	pg.display.update()

	# for loop through the event queue
	for event in pg.event.get():

		# Check for QUIT event
		if event.type == pg.QUIT:
			running = False

