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
        print(end)
        print(renderer)
        self.endPos = end
        self.add_road_layer(renderer)  # Call the method to add road layer

    def add_road_layer(self, renderer):
        print("\n=== DEBUG: Road Generation Started ===")
        print(f"Start: ({self.startPos.x},{self.startPos.y}) → End: ({self.endPos.x},{self.endPos.y})")
        
        currPos = Position(self.startPos.x, self.startPos.y)  
        prevPos = Position(self.startPos.x, self.startPos.y)  
        prevDirection = None
        step = 0

        while currPos != self.endPos:
            if step > 100:  # Prevent infinite loop
                print("Too many steps, breaking.")
                break
            step += 1
            print(f"\nSTEP {step}: At ({currPos.x},{currPos.y})")

            # Store previous position before moving
            prevPos = Position(currPos.x, currPos.y)

            # Calculate possible moves that bring us closer to end
            possible_moves = []
            diff_x = self.endPos.x - currPos.x
            diff_y = self.endPos.y - currPos.y

            # Determine preferred moves based on distance to end
            if abs(diff_x) > abs(diff_y):
                # Prefer horizontal movement
                if diff_x > 0:
                    possible_moves.append(("right", Position(currPos.x + 1, currPos.y)))
                else:
                    possible_moves.append(("left", Position(currPos.x - 1, currPos.y)))
                
                # Add vertical options as secondary
                if diff_y > 0:
                    possible_moves.append(("bottom", Position(currPos.x, currPos.y + 1)))
                elif diff_y < 0:
                    possible_moves.append(("top", Position(currPos.x, currPos.y - 1)))
            else:
                # Prefer vertical movement
                if diff_y > 0:
                    possible_moves.append(("bottom", Position(currPos.x, currPos.y + 1)))
                else:
                    possible_moves.append(("top", Position(currPos.x, currPos.y - 1)))
                
                # Add horizontal options as secondary
                if diff_x > 0:
                    possible_moves.append(("right", Position(currPos.x + 1, currPos.y)))
                elif diff_x < 0:
                    possible_moves.append(("left", Position(currPos.x - 1, currPos.y)))

            # Choose the move that maintains continuity with previous direction when possible
            chosen_move = None
            for move in possible_moves:
                direction, new_pos = move
                # Prefer moves that continue in the same direction
                if prevDirection and direction == prevDirection:
                    chosen_move = move
                    break
            
            # If no continuity move found, choose the first (most optimal) move
            if not chosen_move:
                chosen_move = possible_moves[0]

            direction, new_pos = chosen_move
            currPos = new_pos
            print(f"Moving {direction} to ({currPos.x},{currPos.y})")

            # Determine directions for the road tile
            directions = []
            if prevDirection:
                # Add incoming direction (opposite of previous movement)
                if prevDirection == "right":
                    directions.append("left")
                elif prevDirection == "left":
                    directions.append("right")
                elif prevDirection == "top":
                    directions.append("bottom")
                elif prevDirection == "bottom":
                    directions.append("top")
            
            # Add outgoing direction
            directions.append(direction)

            # Place the road tile at previous position
            print(f"Placing road at ({prevPos.y}, {prevPos.x}) with directions {directions}")
            renderer.place_road(prevPos.y, prevPos.x, directions)

            # Update previous direction for next iteration
            prevDirection = direction

        # Place the final road tile at end position
        final_directions = []
        if prevDirection:
            # Only need incoming direction for the end tile
            if prevDirection == "right":
                final_directions.append("left")
            elif prevDirection == "left":
                final_directions.append("right")
            elif prevDirection == "top":
                final_directions.append("bottom")
            elif prevDirection == "bottom":
                final_directions.append("top")
        
        print(f"Placing final road at ({currPos.y}, {currPos.x}) with directions {final_directions}")
        renderer.place_road(currPos.y, currPos.x, final_directions)