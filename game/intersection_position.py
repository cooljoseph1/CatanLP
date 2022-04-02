from . import constants
from . import tile_position
from . import road_position

class IntersectionPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(("Intersection Position", self.x, self.y))

    def __eq__(self, other):
        return type(self) == type(other) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"IP({self.x}, {self.y})"

    def get_neighboring_intersections(self):
        if self.x & 1:
            return {
                IntersectionPosition(self.x - 1, self.y),
                IntersectionPosition(self.x + 1, self.y),
                IntersectionPosition(self.x - 1, self.y - 1),
            } & constants.ALL_INTERSECTION_POSITIONS
        else:
            return {
                IntersectionPosition(self.x - 1, self.y),
                IntersectionPosition(self.x + 1, self.y),
                IntersectionPosition(self.x + 1, self.y + 1),
            } & constants.ALL_INTERSECTION_POSITIONS

    def get_neighboring_tiles(self):
        if self.x & 1:
            return {
                tile_position.TilePosition(self.x // 2, self.y),
                tile_position.TilePosition(self.x // 2, self.y - 1),
                tile_position.TilePosition(self.x // 2 - 1, self.y - 1),
            } & constants.ALL_TILE_POSITIONS
        else:
            return {
                tile_position.TilePosition(self.x // 2, self.y),
                tile_position.TilePosition(self.x // 2 - 1, self.y),
                tile_position.TilePosition(self.x // 2 - 1, self.y - 1),
            } & constants.ALL_TILE_POSITIONS

    def get_neighboring_roads(self):
        return {
            road_position.RoadPosition(self, other)
            for other in self.get_neighboring_intersections()
        }

    def is_next_to(self, other):
        return other in self.get_neighboring_intersections()

    def is_next_to_tile(self, tilePosition):
        return tilePosition in self.get_neighboring_tiles()

    def is_next_to_road(self, roadPosition):
        return roadPosition in self.get_neighboring_roads()

    def get_render_position(self):
        return (
            (self.x - self.y + 2) * 6,
            ((1 - self.x&1) + 3 * self.y) * 2
        )
