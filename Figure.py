class Figure:
    def __init__(self, type, attributes):
        self.type = type
        self.attributes = attributes

    def tiles_to_visit(self):
        # it returns all tiles that should be visited
        # start position = 0,0
        # ex. [(0,0), (0,1), (1,0), (1,1)] - rectangle 2 x 2
        # XX
        # XX
        # ex2. [(-1,0), (0,0), (1,0), (0,1), (0,-1)] - circle with radius 1
        #  X
        # XXX
        #  X
        if self.type == 'rectangle':
            width = self.attributes['width']
            height = self.attributes['height']
            tiles = []
            for x in range(width):
                for y in range(height):
                    tiles.append((x, y))
            return tiles
        
        if self.type == 'circle':
            radius = self.attributes['radius']
            tiles = []
            for x in range(-radius, radius+1):
                for y in range(-radius, radius+1):
                    if x**2 + y**2 <= radius**2:
                        tiles.append((x, y))
            return tiles