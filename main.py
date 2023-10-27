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


def pixelToCoord(pixel):
	return int(pixel[0]/square_size[0]), int(pixel[1]/square_size[1])


def coordToSquare(coord):
	return 63 - (coord[1] * 8 + coord[0])  # They count the squares up to 64, not using coords


def squareToCoord(square):
	# this depends on how the pieces are transfered from the board: are they mirrored? etc.
	return (63 - square) % 8, (63 - square) // 8


def mouseposToSquare(mousepos):
	coord = pixelToCoord(pg.Vector2(mousepos))
	return coordToSquare(coord)


def draw_piece(piece_key, coord):
	if str(piece_key) == "None":
		return
	try:
		screen.blit(pieceTransforms[str(piece_key)], coordToPixel(coord))
	except KeyError:
		print(str(piece_key), " piece not found")
		pass


def drawAndReturnMoves():
	# Get mouse position
	mousepos = pg.mouse.get_pos()
	text_surface = font.render(str(mousepos), True, (0, 0, 0))  # Text, antialias, color
	text_rect = text_surface.get_rect()
	text_rect.center = (screen_dim // 2)  # Center the text
	screen.blit(text_surface, text_rect)

	coord = pixelToCoord(pg.Vector2(mousepos))
	square = coordToSquare(coord)

	piece = board.piece_at(square)
	print(piece)

	legal_moves = list(board.legal_moves)

	# filters out the legal moves only for that piece, converts from squares to coords, and draws their locations
	piece_moves = []
	for move in legal_moves:
		if move.from_square == square:
			piece_moves.append(move)
			print(f"from square {move.from_square}, to square {move.to_square}")
			dot_coord = squareToCoord(move.to_square)  # convert back to grid coord
			print(dot_coord)
			pos = ((dot_coord[0]+0.5)*square_size[0], (dot_coord[1]+0.5)*square_size[1])
			print("pos: ", pos)
			pg.draw.circle(screen, "purple", pos, 15)

	return piece_moves


def drawBoard():
	screen.fill(background_colour)
	for row in range(0, 8):
		for col in range(0, 8):
			if (row + col) % 2 == 0:
				pg.draw.rect(screen, "white", (row * square_size.x, col * square_size.y, square_size.x, square_size.y))
	for row in range(0, 8):
		for col in range(0, 8):
			draw_piece(str(board.piece_at(63 - (row * 8 + col))), (col, row))



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

drawBoard()
pg.display.update()

highlighted_moves = []

running = True
# game loop
while running:

	# for loop through the event queue
	for event in pg.event.get():

		# Check for QUIT event
		if event.type == pg.QUIT:
			running = False

		# draws board only on mouse click.
		if event.type == pg.MOUSEBUTTONDOWN:
			square = mouseposToSquare(pg.mouse.get_pos())

			moved = False
			for move in highlighted_moves:
				if square == move.to_square:
					board.push(move)
					moved = True
				drawBoard()
			if not moved:
				drawBoard()
				highlighted_moves = drawAndReturnMoves()

			pg.display.update()

