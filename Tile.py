from twisted.test.raiser import raiseException

from Raiser import Raiser

class Tile:
    def __init__(self, args=[],ctx=None):
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

            self.add_obj(arg[0],ctx)

    def remove_foreground (self):
        self.foreground = None
    
    def add_obj(self, obj,ctx=None):
        if obj in ['grass', 'soil', 'sand', 'water', 'rocks']:
            self.background = obj
        elif obj in ['tree', 'bush', 'stones', 'mountains', 'cabin', 'church']:
            self.foreground = obj
        else:
            if ctx == None:
                print(ctx)
                raise Exception(f"'{obj}' is not a valid tile object")
            else:
                Raiser.raiseError(ctx,f"'{obj}' is not a valid tile object")

    def get_road_image(self):
        if(self.road_directions['top'] and self.road_directions['bottom'] and self.road_directions['left'] and self.road_directions['right']):
            self.road = "cross"
        # 3 directions
        elif (self.road_directions['top'] and self.road_directions['bottom'] and self.road_directions['left']):
            self.road = "noR"
        elif (self.road_directions['top'] and self.road_directions['bottom'] and self.road_directions['right']):
            self.road = "noL"
        elif (self.road_directions['top'] and self.road_directions['left'] and self.road_directions['right']):
            self.road = "noB"
        elif (self.road_directions['bottom'] and self.road_directions['left'] and self.road_directions['right']):
            self.road = "noT"
        # 2 directions
        elif(self.road_directions['top'] and self.road_directions['bottom']):
            self.road = "vertical"
        elif(self.road_directions['left'] and self.road_directions['right']):
            self.road = "horizontal"
        elif(self.road_directions['top']):
            if(self.road_directions['left']):
                self.road = "tl"
            if(self.road_directions['right']):
                self.road = "tr"
        elif(self.road_directions['bottom']):
            if(self.road_directions['left']):
                self.road = "bl"
            if(self.road_directions['right']):
                self.road = "br"
        if(self.road): print(f"Road image: {self.road}")

    def add_road(self, directions):
        for direction in ['top', 'bottom', 'left', 'right']:
            if(direction in directions):
                self.road_directions[direction] = True
        self.get_road_image()



    def __str__(self):
        return self.background + (("+"+self.foreground) if self.foreground else "")