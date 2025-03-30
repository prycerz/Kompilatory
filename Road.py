import numpy as np
import MapperRenderer
class Position:
    def __init__(self, s_x, s_y):
        self.s_x = s_x
        self.s_y = s_y

    def end(self, e_x, e_y):
        self.e_x = e_x
        self.e_y = e_y

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

    def end(self, end: Position):
        self.endPos = end

    def detect_bend(pos1, pos2, pos3):
        """
        Detects the direction of movement based on three consecutive positions.
        Returns one of: "horizontal", "vertical", "upRight", "downRight", "upLeft", "downLeft", or "straight".
        """
        dx1, dy1 = pos2.x - pos1.x, pos2.y - pos1.y
        dx2, dy2 = pos3.x - pos2.x, pos3.y - pos2.y

        if dx1 == dx2 and dy1 == dy2:
            return "noBend"

        if dx2 == 0:
            return "vertical"
        if dy2 == 0:
            return "horizontal"

        if dx1 < dx2 and dy1 < dy2:
            return "upRight"
        if dx1 < dx2 and dy1 > dy2:
            return "downRight"
        if dx1 > dx2 and dy1 < dy2:
            return "upLeft"
        if dx1 > dx2 and dy1 > dy2:
            return "downLeft"

        return "unknown"  # Catch-all case

    def tiles_to_visit_(self, map):
        bias = 0.3
        random_num = np.random(0,1)
        currPos = self.startPos
        prevPos = self.startPos
        prevprevPos = self.startPos
        while(currPos!=self.endPos):
            prevprevPos = prevPos
            prevPos = currPos
            random_num = np.random.normal(0, 1)
            diff_vector = Position.difference(currPos,self.endPos)
            #aim to minimize the bigger of the two
            if(random_num>bias):
                if abs(diff_vector.x) > abs(diff_vector.y):
                    currPos.x += diff_vector.x // abs(diff_vector.x)
                else:
                    currPos.y += currPos.y + diff_vector.y // abs(diff_vector.y)
            else:
                if np.random.rand() > 0.5:
                    currPos.x += np.random.choice([-1, 1])
                else:
                    currPos.y += np.random.choice([-1, 1])
            bend = self.detect_bend(prevprevPos, prevPos, currPos)
            if(bend == "noBend"):
                continue
            else:
                MapperRenderer.placeRoad(prevPos.e_y,prevPos.e_x,bend)





        # it returns all tiles that should be visited
        # start position = 0,0
        # ex. [(0,0), (0,1), (1,0), (1,1)] - rectangle 2 x 2
        # XX
        # XX
        # ex2. [(-1,0), (0,0), (1,0), (0,1), (0,-1)] - circle with radius 1
        #  X
        # XXX
        #  X
