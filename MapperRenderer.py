import pygame
from Cython import pointer

from Blend import Blend
from Tile import Tile
# Ustawienia ekranu
TILE_SIZE = 32
MAP_WIDTH = 40  # 40 * 32 = 1280px
MAP_HEIGHT = 25  # 25 * 32 = 804px
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
			"tree": pygame.image.load('assets/foreground/tree.png').convert_alpha(),
		}

		self.ROAD_TILE_IMAGES = {
			"cross": pygame.image.load('assets/road/cross.png').convert_alpha(),
			"bl": pygame.image.load('assets/road/bl.png').convert_alpha(),
			"br": pygame.image.load('assets/road/br.png').convert_alpha(),
			"tl": pygame.image.load('assets/road/tl.png').convert_alpha(),
			"tr": pygame.image.load('assets/road/tr.png').convert_alpha(),
			"noT": pygame.image.load('assets/road/noT.png').convert_alpha(),
			"noB": pygame.image.load('assets/road/noB.png').convert_alpha(),
			"noL": pygame.image.load('assets/road/noL.png').convert_alpha(),
			"noR": pygame.image.load('assets/road/noR.png').convert_alpha(),
			"vertical": pygame.image.load('assets/road/vertical.png').convert_alpha(),
			"horizontal": pygame.image.load('assets/road/horizontal.png').convert_alpha(),
		}

		self.clock = pygame.time.Clock()
		self.pointer_x, self.pointer_y = int(MAP_WIDTH/2), int(MAP_HEIGHT/2)  # Startowa pozycja wskaźnika
		# fill map_data with waterTile
		self.reset_map()


	def move_pointer(self, dx, dy):
		self.pointer_x = max(0, min(MAP_WIDTH - 1, self.pointer_x + dx))
		self.pointer_y = max(0, min(MAP_HEIGHT - 1, self.pointer_y + dy))


	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		pygame.display.flip()


	def copy_tile(self, x, y, tile : Tile):
		# debug
		print(f'copying tile {tile} to {y}, {x}')
		# size of map
		print(f'map size: {len(self.map_data)}, {len(self.map_data[0])}')

		self.map_data[y][x].add_obj(tile.background)
		
		if tile.foreground:
			self.map_data[y][x].add_obj(tile.foreground)
		else: 
			self.map_data[y][x].remove_foreground()

	# NOT OVERRITE TILE, JUST REPLACE BY ADDING OBJECTS - to make sure roads are not overwritten
	def draw_tile(self, tile):
		if isinstance(tile, Tile):
			self.copy_tile(self.pointer_x, self.pointer_y, tile)
		elif isinstance(tile, Blend):
			for x, y in tile.figure.tiles_to_visit():
				self.copy_tile(self.pointer_x + x, self.pointer_y + y, tile.random_tile())
		self.render()  # Force an update on screen


	def place_road(self, y, x, directions):
		self.map_data[y][x].add_road(directions)
		self.render()

	def render(self):
		self.screen.fill((0, 0, 0))  # Clear screen
		# print('RENDERING')
		for y, row in enumerate(self.map_data):
			for x, tile in enumerate(row):
				if isinstance(tile, Tile):
					self.screen.blit(self.BACKGROUND_TILE_IMAGES[tile.background], (x * TILE_SIZE, y * TILE_SIZE))


					if tile.road:
						road_image = self.ROAD_TILE_IMAGES[tile.road]
						scaled_road_image = pygame.transform.scale(road_image, (TILE_SIZE, TILE_SIZE))
						self.screen.blit(scaled_road_image, (x * TILE_SIZE, y * TILE_SIZE))
					
					elif tile.foreground:
						image = self.FOREGROUND_TILE_IMAGES[tile.foreground]
						scaled_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
						self.screen.blit(scaled_image, (x * TILE_SIZE, y * TILE_SIZE))
				
					
		pygame.display.flip()  # Update display


	def reset_map(self):
		self.map_data = [[Tile() for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
		for row in self.map_data:
			for tile in row:
				tile.add_obj('water')
		self.pointer_x, self.pointer_y = int(MAP_WIDTH/2), int(MAP_HEIGHT/2)
		self.render()

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
