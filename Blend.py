import random

class Blend:
    def __init__(self, figure, percentages):
        self.figure = figure
        self.percentages = percentages

    def _normalize_percentages(self):
        total_percentage = sum(percentage for tile, percentage in self.percentages)
        
        if total_percentage < 100:
            # If total is less than 100%, fill with grass
            self.percentages.append(('grass', 100 - total_percentage))
        elif total_percentage > 100:
            raise ValueError("Total percentages cannot exceed 100%.")
    
    def random_tile(self):
        # Returns a random tile based on the percentages
        # Example: percentages = [('grass', 50), ('water', 50)]
        # It returns 'grass' with a 50% chance and 'water' with a 50% chance
        tiles = [tile.__str__() for tile, percentage in self.percentages]
        weights = [percentage for tile, percentage in self.percentages]
        
        return random.choices(tiles, weights)[0]
