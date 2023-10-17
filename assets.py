import pygame
pieceImgs = {}
for name in ("K","k","Q","q","R", "r", "B","b", "N", "n", "P", "p"):
	try:
		pieceImgs[name] = pygame.image.load(f"assets/{name}.svg")
	except FileNotFoundError:
		print("Piece image not found")
