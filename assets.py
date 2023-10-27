import pygame
pieceImgs = {}
for piece_libname, svg_name in (("K", "kw"),
								("k","kb"),
								("Q","qw"),
								("q","qb"),
								("R","rw"),
								("r","rb"),
								("B","bw"),
								("b","bb"),
								("N","nw"),
								("n","nb"),
								("P","pw"),
								("p","pb")):
	try:
		pieceImgs[piece_libname] = pygame.image.load(f"assets/{svg_name}.svg")
	except FileNotFoundError:
		print("Piece image not found")

# By Cburnett - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1499806


numCoordToChessCoord = {}
