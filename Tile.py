class Tile:
    def __init__(self, args=[]):
        self.background = 'grass'
        self.foreground = None

        for arg in args:
            if arg in ['grass', 'soil', 'sand', 'water', 'rocks']:
                self.background = arg
            elif arg in ['tree', 'bush', 'stones', 'mountains', 'cabin', 'church']:
                self.foreground = arg