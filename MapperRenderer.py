import pygame
from Cython import pointer

from Blend import Blend
from Tile import Tile
# Ustawienia ekranu
TILE_SIZE = 32
MAP_WIDTH = 25  # 25x32 = 800px
MAP_HEIGHT = 18  # 18x32 = 576px
WINDOW_WIDTH = MAP_WIDTH * TILE_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * TILE_SIZE

class MapperRenderer:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.BACKGROUND_TILE_IMAGES = {
			"grass": pygame.image.load('assets/background/grass.png').convert_alpha(),
			"sand": pygame.image.load('assets/background/sand.png').convert_alpha(),
			"water": pygame.image.load('assets/background/water.png').convert_alpha(),
			"rocks": pygame.image.load('assets/background/rocks.png').convert_alpha(),
			"soil": pygame.image.load('assets/background/soil.png').convert_alpha(),
		}

		self.FOREGROUND_TILE_IMAGES = {
			"tree": pygame.image.load('assets/foreground/tree.png').convert_alpha(),
			"stones": pygame.image.load('assets/foreground/stones.png').convert_alpha(),
			"cabin": pygame.image.load('assets/foreground/cabin.png').convert_alpha(),
			"bush": pygame.image.load('assets/foreground/bush.png').convert_alpha(),
			"mountains": pygame.image.load('assets/foreground/mountains.png').convert_alpha(),
			"church": pygame.image.load('assets/foreground/church.png').convert_alpha(),
		}


		self.clock = pygame.time.Clock()
		self.pointer_x, self.pointer_y = 5, 5  # Startowa pozycja wskaźnika
		self.map_data = [["water"] * MAP_WIDTH for _ in range(MAP_HEIGHT)]  # Mapa początkowo zalana wodą


	def move_pointer(self, dx, dy):
		self.pointer_x = max(0, min(MAP_WIDTH - 1, self.pointer_x + dx))
		self.pointer_y = max(0, min(MAP_HEIGHT - 1, self.pointer_y + dy))

	def draw_tile(self, tile):
		# Deprecated
		# if isinstance(tile, str):
		# 	self.map_data[self.pointer_y][self.pointer_x] = tile
		if isinstance(tile, Tile):
			self.map_data[self.pointer_y][self.pointer_x] = tile.background + (("+"+tile.foreground) if tile.foreground else "")
		elif isinstance(tile, Blend):
			"""
			TODO: narysować wypełnione koło
			"""
			self.render()
		self.render()  # Force an update on screen

	def render(self):
		self.screen.fill((0, 0, 0))  # Clear screen

		for y, row in enumerate(self.map_data):
			for x, tile_name in enumerate(row):
				objectsArray = tile_name.split('+')
				for obj in objectsArray:
					if(obj in self.BACKGROUND_TILE_IMAGES):
						image = self.BACKGROUND_TILE_IMAGES[obj]
						self.screen.blit(image, (x * TILE_SIZE, y * TILE_SIZE))

					elif(obj in self.FOREGROUND_TILE_IMAGES):
						image = self.FOREGROUND_TILE_IMAGES[obj]
						scaled_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
						self.screen.blit(scaled_image, (x * TILE_SIZE, y * TILE_SIZE))

		pygame.display.flip()  # Update display

	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False  # Close window when user clicks 'X'
			pygame.display.flip()  # Continuously update display

		pygame.quit()  # Properly exit Pygame when loop ends


if __name__ == "__main__":
	renderer = MapperRenderer()
	renderer.run()
