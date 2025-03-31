class RoadTile:
    def __init__(self):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

    def configure(self, directions):
        for direction in ['top', 'bottom', 'left', 'right']:
            if(directions[direction]):
                setattr(self, direction, True)