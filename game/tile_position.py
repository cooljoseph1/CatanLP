from . import constants
from . import intersection_position

class TilePosition:
    NEIGHBOR_DIFFS = {
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
    }

    INTERSECTION_DIFFS = {
        (0, 0),
        (1, 0),
        (2, 0),
        (1, 1),
        (2, 1),
        (3, 1),
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(("Tile Position", self.x, self.y))

    def __eq__(self, other):
        return type(self) == type(other) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"TP({self.x}, {self.y})"

    def get_neighboring_tiles(self):
        return {
            TilePosition(self.x + diff[0], self.y + diff[1])
            for diff in TilePosition.NEIGHBOR_DIFFS
        } & constants.ALL_TILE_POSITIONS

    def get_neighboring_intersections(self):
        return {
            intersection_position.IntersectionPosition(2 * self.x + diff[0], self.y + diff[1])
            for diff in TilePosition.INTERSECTION_DIFFS
        }

    def is_next_to(self, other):
        return other in self.get_neighboring_tiles()

    def is_next_to_intersection(self, intersectionPosition):
        return intersectionPosition in self.get_neighboring_intersections()

    def get_render_position(self):
        return ((self.x * 2 - self.y + 3) * 6, (self.y * 3 + 2) * 2)
