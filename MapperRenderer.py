import pygame
from Tile import Tile
# Ustawienia ekranu
TILE_SIZE = 32
MAP_WIDTH = 25  # 25x32 = 800px
MAP_HEIGHT = 18  # 18x32 = 576px
WINDOW_WIDTH = MAP_WIDTH * TILE_SIZE
WINDOW_HEIGHT = MAP_HEIGHT * TILE_SIZE

# Kolory dla płytek
TILE_COLORS = {
	"grass": (34, 139, 34),
	"sand": (210, 180, 140),
	"water": (0, 191, 255),
	"tree": (139, 69, 19),
	"rock": (105, 105, 105),
	"cabin": (160, 82, 45),
	"grass+tree": (100,100,100)
}

class MapperRenderer:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.pointer_x, self.pointer_y = 5, 5  # Startowa pozycja wskaźnika
		self.map_data = [["water"] * MAP_WIDTH for _ in range(MAP_HEIGHT)]  # Mapa początkowo zalana wodą


	def draw_map(self):
		self.screen.fill((0, 0, 0))  # Czyszczenie ekranu

		# Rysowanie płytek
		for y in range(MAP_HEIGHT):
			for x in range(MAP_WIDTH):
				tile_type = self.map_data[y][x]
				color = TILE_COLORS.get(tile_type, (255, 255, 255))  # Domyślnie biały
				pygame.draw.rect(self.screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

		# Rysowanie wskaźnika (czerwony kwadrat)
		pygame.draw.rect(self.screen, (255, 0, 0), (self.pointer_x * TILE_SIZE, self.pointer_y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)

		pygame.display.flip()

	def move_pointer(self, dx, dy):
		self.pointer_x = max(0, min(MAP_WIDTH - 1, self.pointer_x + dx))
		self.pointer_y = max(0, min(MAP_HEIGHT - 1, self.pointer_y + dy))

	def draw_tile(self, tile):
		if isinstance(tile,str):
			if tile in TILE_COLORS:
				print(f"drawing tile {tile}")
				self.map_data[self.pointer_y][self.pointer_x] = tile


		elif isinstance(tile,Tile):
			self.map_data[self.pointer_y][self.pointer_x] = tile.background + (tile.foreground if tile.foreground else "")

		self.render()  # Force an update on screen

	def render(self):
		self.screen.fill((0, 0, 0))  # Clear screen

		for y, row in enumerate(self.map_data):
			for x, tile_name in enumerate(row):
				if tile_name in TILE_COLORS:
					color = TILE_COLORS[tile_name]
					pygame.draw.rect(self.screen, color,
									 pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

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
