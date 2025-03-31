import numpy as np
from MapperRenderer import MapperRenderer

class Position:
    def __init__(self, s_x, s_y):
        self.x = s_x
        self.y = s_y

    @staticmethod
    def difference(pos1, pos2):
        """Returns a Position representing the difference vector (pos2 - pos1)."""
        if isinstance(pos1, Position) and isinstance(pos2, Position):
            return Position(pos2.x - pos1.x, pos2.y - pos1.y)
        raise TypeError("Both arguments must be Position objects")

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

class Road:
    def __init__(self, start: Position):
        self.startPos = start
        self.endPos = None  # End position is initially unset

    def end(self, end: Position, renderer: MapperRenderer):
        self.endPos = end
        self.add_road_layer(renderer)  # Call the method to add road layer

    def add_road_layer(self, renderer):

        print("\n=== DEBUG: Road Generation Started ===")
        print(f"Start: ({self.startPos.x},{self.startPos.y}) → End: ({self.endPos.x},{self.endPos.y})")
        
        currPos = Position(self.startPos.x, self.startPos.y)  
        prevPos = None
        step = 0

        while currPos != self.endPos:
            if step > 100:
                print("Too many steps, breaking.")
                break
            
            step += 1
            print(f"\nSTEP {step}: At ({currPos.x},{currPos.y})")

            diff_vector = Position.difference(currPos, self.endPos)

            if(np.random.rand() < abs(diff_vector.x) / (abs(diff_vector.x) + abs(diff_vector.y))):
                # then move x
                move_x = diff_vector.x // abs(diff_vector.x)  # Ensure not dividing by zero
                currPos.x += move_x
                print(f"Move x: {move_x}")
            else:
                move_y = diff_vector.y // abs(diff_vector.y)
                currPos.y += move_y
                print(f"Move y: {move_y}")

            renderer.place_road(currPos.y, currPos.x)

            # # Determine FROM direction (previous movement)
            # if currPos.x > prevPos.x:
            #     renderer.place_road(prevPos.y, prevPos.x, "right")
            #     renderer.place_road(currPos.y, currPos.x, "left")
            #     print("Move right")
            # elif currPos.x < prevPos.x:
            #     renderer.place_road(prevPos.y, prevPos.x, "left")
            #     renderer.place_road(currPos.y, currPos.x, "right")
            #     print("Move left")
            # elif currPos.y < prevPos.y:
            #     renderer.place_road(prevPos.y, prevPos.x, 'top')
            #     renderer.place_road(currPos.y, currPos.x, "bottom")
            #     print("Move up")
            # elif currPos.y > prevPos.y:
            #     renderer.place_road(prevPos.y, prevPos.x, "bottom")
            #     renderer.place_road(currPos.y, currPos.x, "top")
            #     print("Move down")