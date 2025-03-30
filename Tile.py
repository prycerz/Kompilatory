class Tile:
    def __init__(self, args=[]):
        self.background = 'grass'
        self.foreground = None

        for arg in args:
            self.add_obj(arg)
    
    def add_obj(self, obj):
        if obj in ['grass', 'soil', 'sand', 'water', 'rocks']:
            self.background = obj
        elif obj in ['tree', 'bush', 'stones', 'mountains', 'cabin', 'church','horizontal', 'vertical', 'upRight', 'downRight', 'upLeft', 'downLeft']:
            self.foreground = obj

    def __str__(self):
        return self.background + (("+"+self.foreground) if self.foreground else "")