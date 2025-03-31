class Tile:
    def __init__(self, args=[]):
        self.background = 'grass'
        self.foreground = None
        self.road = None
        # ROAD
        self.road_directions = {
            'top': False,
            'bottom': False,
            'left': False,
            'right': False
        }

        for arg in args:
            self.add_obj(arg)

    def remove_foreground (self):
        self.foreground = None
    
    def add_obj(self, obj):
        if obj in ['grass', 'soil', 'sand', 'water', 'rocks']:
            self.background = obj
        elif obj in ['tree', 'bush', 'stones', 'mountains', 'cabin', 'church']:
            self.foreground = obj

    
        # if(self.road): print(f"Road image: {self.road}")

    def add_road(self):
        self.road = True

    def __str__(self):
        return self.background + (("+"+self.foreground) if self.foreground else "")