import chess
import pygame as pg

# create board object
board = chess.Board()

# display chess board
print(board)

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen_dim = (600,600)
screen = pg.display.set_mode(screen_dim)

# Set the caption of the screen
pg.display.set_caption('Geeksforgeeks')


# Fill the background colour to the screen

# Update the display using flip
pg.display.flip()

# Variable to keep our game loop running
running = True

square_size = screen_dim[0]/8

# game loop
while running:
	screen.fill(background_colour)
	for x in range(8):
		for y in range(8):
			if (x+y)%2 == 0:
				continue
			pg.draw.rect(screen, "white", (x*square_size, y*square_size, square_size, square_size))
			print(x, y)

	pg.display.update()

	# for loop through the event queue
	for event in pg.event.get():

		# Check for QUIT event
		if event.type == pg.QUIT:
			running = False
