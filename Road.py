import numpy as np
from numpy import random
from MapperRenderer import MapperRenderer

class Position:
    def __init__(self, s_x, s_y):
        self.x = s_x
        self.y = s_y

    @staticmethod
    def difference(pos1, pos2):
        """Returns a Position representing the difference vector (pos2 - pos1)."""
        if isinstance(pos1, Position) and isinstance(pos2, Position):
            return Position(abs(pos2.x - pos1.x), abs(pos2.y - pos1.y))
        raise TypeError("Both arguments must be Position objects")

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

class Road:
    def __init__(self, start: Position):
        self.startPos = start
        self.endPos = None  # End position is initially unset

    def end(self, end: Position, renderer : MapperRenderer):
        self.endPos = end
        self.add_road_layer(renderer)  # Call the method to add road layer

    def detect_bend(self, pos1, pos2, pos3):
        """
        Detects all possible bend directions between three consecutive positions.
        Returns: "rightUp", "rightDown", "leftUp", "leftDown",
                 "upRight", "upLeft", "downRight", "downLeft",
                 "horizontal", "vertical", or "noBend"
        """
        # Calculate direction vectors
        vec1 = (pos2.x - pos1.x, pos2.y - pos1.y)  # First segment
        vec2 = (pos3.x - pos2.x, pos3.y - pos2.y)  # Second segment

        # No direction change
        if vec1 == vec2:
            return "noBend"

        # Horizontal movement
        if vec1[1] == 0 and vec2[1] == 0:
            return "horizontal"

        # Vertical movement
        if vec1[0] == 0 and vec2[0] == 0:
            return "vertical"

        # Diagonal bends (8 possible directions)
        # Rightward initial movement
        if vec1[0] > 0:
            if vec2[1] < 0: return "rightUp"
            if vec2[1] > 0: return "rightDown"

        # Leftward initial movement
        elif vec1[0] < 0:
            if vec2[1] < 0: return "leftUp"
            if vec2[1] > 0: return "leftDown"

        # Upward initial movement
        if vec1[1] < 0:
            if vec2[0] > 0: return "upRight"
            if vec2[0] < 0: return "upLeft"

        # Downward initial movement
        elif vec1[1] > 0:
            if vec2[0] > 0: return "downRight"
            if vec2[0] < 0: return "downLeft"

        return "noBend"  # Default case

    def add_road_layer (self, renderer):
        print("\n=== DEBUG: Road Generation Started ===")
        print(f"Start: ({self.startPos.x},{self.startPos.y}) → End: ({self.endPos.x},{self.endPos.y})")
        
        bias = 0.1
        currPos = Position(self.startPos.x, self.startPos.y)  
        prevPos = Position(self.startPos.x, self.startPos.y)  
        prevprevPos = Position(self.startPos.x, self.startPos.y)  
        step = 0

        while currPos != self.endPos:
            if step > 100:
                print("Too many steps, breaking.")
                break
            step += 1
            print(f"\nSTEP {step}: At ({currPos.x},{currPos.y})")

            prevprevPos = Position(prevPos.x, prevPos.y)
            prevPos = Position(currPos.x, currPos.y)

            random_num = np.random.random()
            diff_vector = Position.difference(currPos, self.endPos)

            print(f"Random: {random_num:.2f}, Diff: ({diff_vector.x},{diff_vector.y})")

            if random_num > bias:
                if abs(diff_vector.x) > abs(diff_vector.y):
                    currPos.x += diff_vector.x // abs(diff_vector.x)
                    print("Move x")
                else:
                    currPos.y -= diff_vector.y // abs(diff_vector.y)
                    print("Move y")
            else:
                print("Random choice")
                if np.random.random() > 0.5:
                    currPos.x += np.random.choice([-1, 1])
                else:
                    currPos.y += np.random.choice([-1, 1])

            # Track both FROM and TO directions
            directions = {}

            # Determine FROM direction (previous movement)
            if prevPos.x > prevprevPos.x:
                directions["right"] = True
            elif prevPos.x < prevprevPos.x:
                directions["left"] = True

            if prevPos.y > prevprevPos.y:
                directions["bottom"] = True
            elif prevPos.y < prevprevPos.y:
                directions["top"] = True

            # Determine TO direction (current movement)
            if currPos.x > prevPos.x:
                directions["right"] = True
            elif currPos.x < prevPos.x:
                directions["left"] = True

            if currPos.y > prevPos.y:
                directions["bottom"] = True
            elif currPos.y < prevPos.y:
                directions["top"] = True

            # Convert dictionary keys to a list of strings
            direction_list = list(directions.keys())

            print(f"Placing road at ({prevPos.y}, {prevPos.x}) with directions {direction_list}")
            renderer.place_road(prevPos.y, prevPos.x, direction_list)