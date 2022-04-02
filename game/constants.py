from .resource import Resource
from .tile_position import TilePosition
from .intersection_position import IntersectionPosition
from .road_position import RoadPosition

BRICK_TILES = 3
DESERT_TILES = 1
LUMBER_TILES = 4
ORE_TILES = 3
WHEAT_TILES = 4
WOOL_TILES = 4

ALL_RESOURCE_TYPES = (
    Resource.BRICK,
    Resource.LUMBER,
    Resource.ORE,
    Resource.WHEAT,
    Resource.WOOL,
)

ALL_TILE_POSITIONS = {
    TilePosition(0, 0),
    TilePosition(1, 0),
    TilePosition(2, 0),

    TilePosition(0, 1),
    TilePosition(1, 1),
    TilePosition(2, 1),
    TilePosition(3, 1),

    TilePosition(0, 2),
    TilePosition(1, 2),
    TilePosition(2, 2),
    TilePosition(3, 2),
    TilePosition(4, 2),

    TilePosition(1, 3),
    TilePosition(2, 3),
    TilePosition(3, 3),
    TilePosition(4, 3),

    TilePosition(2, 4),
    TilePosition(3, 4),
    TilePosition(4, 4),
}

ALL_INTERSECTION_POSITIONS = {
    IntersectionPosition(0, 0),
    IntersectionPosition(1, 0),
    IntersectionPosition(2, 0),
    IntersectionPosition(3, 0),
    IntersectionPosition(4, 0),
    IntersectionPosition(5, 0),
    IntersectionPosition(6, 0),
    IntersectionPosition(0, 1),
    IntersectionPosition(1, 1),
    IntersectionPosition(2, 1),
    IntersectionPosition(3, 1),
    IntersectionPosition(4, 1),
    IntersectionPosition(5, 1),
    IntersectionPosition(6, 1),
    IntersectionPosition(7, 1),
    IntersectionPosition(8, 1),
    IntersectionPosition(0, 2),
    IntersectionPosition(1, 2),
    IntersectionPosition(2, 2),
    IntersectionPosition(3, 2),
    IntersectionPosition(4, 2),
    IntersectionPosition(5, 2),
    IntersectionPosition(6, 2),
    IntersectionPosition(7, 2),
    IntersectionPosition(8, 2),
    IntersectionPosition(9, 2),
    IntersectionPosition(10, 2),
    IntersectionPosition(1, 3),
    IntersectionPosition(2, 3),
    IntersectionPosition(3, 3),
    IntersectionPosition(4, 3),
    IntersectionPosition(5, 3),
    IntersectionPosition(6, 3),
    IntersectionPosition(7, 3),
    IntersectionPosition(8, 3),
    IntersectionPosition(9, 3),
    IntersectionPosition(10, 3),
    IntersectionPosition(11, 3),
    IntersectionPosition(3, 4),
    IntersectionPosition(4, 4),
    IntersectionPosition(5, 4),
    IntersectionPosition(6, 4),
    IntersectionPosition(7, 4),
    IntersectionPosition(8, 4),
    IntersectionPosition(9, 4),
    IntersectionPosition(10, 4),
    IntersectionPosition(11, 4),
    IntersectionPosition(5, 5),
    IntersectionPosition(6, 5),
    IntersectionPosition(7, 5),
    IntersectionPosition(8, 5),
    IntersectionPosition(9, 5),
    IntersectionPosition(10, 5),
    IntersectionPosition(11, 5),
}

ALL_ROAD_POSITIONS = {
    RoadPosition(
              IntersectionPosition(5, 0),
              IntersectionPosition(4, 0)
    ),
    RoadPosition(
              IntersectionPosition(3, 0),
              IntersectionPosition(2, 0)
    ),
    RoadPosition(
              IntersectionPosition(6, 0),
              IntersectionPosition(5, 0)
    ),
    RoadPosition(
              IntersectionPosition(1, 0),
              IntersectionPosition(0, 0)
    ),
    RoadPosition(
              IntersectionPosition(3, 0),
              IntersectionPosition(4, 0)
    ),
    RoadPosition(
              IntersectionPosition(2, 0),
              IntersectionPosition(1, 0)
    ),
    RoadPosition(
              IntersectionPosition(2, 0),
              IntersectionPosition(3, 1)
    ),
    RoadPosition(
              IntersectionPosition(7, 1),
              IntersectionPosition(6, 1)
    ),
    RoadPosition(
              IntersectionPosition(5, 1),
              IntersectionPosition(4, 0)
    ),
    RoadPosition(
              IntersectionPosition(5, 1),
              IntersectionPosition(6, 1)
    ),
    RoadPosition(
              IntersectionPosition(4, 1),
              IntersectionPosition(5, 2)
    ),
    RoadPosition(
              IntersectionPosition(4, 1),
              IntersectionPosition(3, 1)
    ),
    RoadPosition(
              IntersectionPosition(6, 1),
              IntersectionPosition(7, 2)
    ),
    RoadPosition(
              IntersectionPosition(2, 1),
              IntersectionPosition(3, 2)
    ),
    RoadPosition(
              IntersectionPosition(7, 1),
              IntersectionPosition(8, 1)
    ),
    RoadPosition(
              IntersectionPosition(1, 1),
              IntersectionPosition(0, 0)
    ),
    RoadPosition(
              IntersectionPosition(7, 1),
              IntersectionPosition(6, 0)
    ),
    RoadPosition(
              IntersectionPosition(4, 1),
              IntersectionPosition(5, 1)
    ),
    RoadPosition(
              IntersectionPosition(1, 1),
              IntersectionPosition(2, 1)
    ),
    RoadPosition(
              IntersectionPosition(1, 1),
              IntersectionPosition(0, 1)
    ),
    RoadPosition(
              IntersectionPosition(2, 1),
              IntersectionPosition(3, 1)
    ),
    RoadPosition(
              IntersectionPosition(6, 2),
              IntersectionPosition(7, 2)
    ),
    RoadPosition(
              IntersectionPosition(9, 2),
              IntersectionPosition(8, 2)
    ),
    RoadPosition(
              IntersectionPosition(8, 2),
              IntersectionPosition(7, 2)
    ),
    RoadPosition(
              IntersectionPosition(4, 2),
              IntersectionPosition(5, 3)
    ),
    RoadPosition(
              IntersectionPosition(1, 2),
              IntersectionPosition(0, 1)
    ),
    RoadPosition(
              IntersectionPosition(4, 2),
              IntersectionPosition(5, 2)
    ),
    RoadPosition(
              IntersectionPosition(0, 2),
              IntersectionPosition(1, 3)
    ),
    RoadPosition(
              IntersectionPosition(3, 2),
              IntersectionPosition(2, 2)
    ),
    RoadPosition(
              IntersectionPosition(6, 2),
              IntersectionPosition(5, 2)
    ),
    RoadPosition(
              IntersectionPosition(9, 2),
              IntersectionPosition(10, 2)
    ),
    RoadPosition(
              IntersectionPosition(8, 2),
              IntersectionPosition(9, 3)
    ),
    RoadPosition(
              IntersectionPosition(6, 2),
              IntersectionPosition(7, 3)
    ),
    RoadPosition(
              IntersectionPosition(1, 2),
              IntersectionPosition(2, 2)
    ),
    RoadPosition(
              IntersectionPosition(9, 2),
              IntersectionPosition(8, 1)
    ),
    RoadPosition(
              IntersectionPosition(4, 2),
              IntersectionPosition(3, 2)
    ),
    RoadPosition(
              IntersectionPosition(1, 2),
              IntersectionPosition(0, 2)
    ),
    RoadPosition(
              IntersectionPosition(10, 3),
              IntersectionPosition(9, 3)
    ),
    RoadPosition(
              IntersectionPosition(10, 3),
              IntersectionPosition(11, 3)
    ),
    RoadPosition(
              IntersectionPosition(8, 3),
              IntersectionPosition(9, 3)
    ),
    RoadPosition(
              IntersectionPosition(3, 3),
              IntersectionPosition(2, 2)
    ),
    RoadPosition(
              IntersectionPosition(2, 3),
              IntersectionPosition(3, 4)
    ),
    RoadPosition(
              IntersectionPosition(4, 3),
              IntersectionPosition(5, 3)
    ),
    RoadPosition(
              IntersectionPosition(11, 3),
              IntersectionPosition(10, 2)
    ),
    RoadPosition(
              IntersectionPosition(2, 3),
              IntersectionPosition(1, 3)
    ),
    RoadPosition(
              IntersectionPosition(8, 3),
              IntersectionPosition(9, 4)
    ),
    RoadPosition(
              IntersectionPosition(6, 3),
              IntersectionPosition(7, 3)
    ),
    RoadPosition(
              IntersectionPosition(2, 3),
              IntersectionPosition(3, 3)
    ),
    RoadPosition(
              IntersectionPosition(5, 3),
              IntersectionPosition(6, 3)
    ),
    RoadPosition(
              IntersectionPosition(3, 3),
              IntersectionPosition(4, 3)
    ),
    RoadPosition(
              IntersectionPosition(10, 3),
              IntersectionPosition(11, 4)
    ),
    RoadPosition(
              IntersectionPosition(7, 3),
              IntersectionPosition(8, 3)
    ),
    RoadPosition(
              IntersectionPosition(4, 4),
              IntersectionPosition(3, 4)
    ),
    RoadPosition(
              IntersectionPosition(7, 4),
              IntersectionPosition(8, 4)
    ),
    RoadPosition(
              IntersectionPosition(7, 4),
              IntersectionPosition(6, 4)
    ),
    RoadPosition(
              IntersectionPosition(11, 4),
              IntersectionPosition(10, 4)
    ),
    RoadPosition(
              IntersectionPosition(9, 4),
              IntersectionPosition(8, 4)
    ),
    RoadPosition(
              IntersectionPosition(7, 4),
              IntersectionPosition(6, 3)
    ),
    RoadPosition(
              IntersectionPosition(5, 4),
              IntersectionPosition(4, 4)
    ),
    RoadPosition(
              IntersectionPosition(10, 4),
              IntersectionPosition(9, 4)
    ),
    RoadPosition(
              IntersectionPosition(5, 4),
              IntersectionPosition(4, 3)
    ),
    RoadPosition(
              IntersectionPosition(6, 4),
              IntersectionPosition(5, 4)
    ),
    RoadPosition(
              IntersectionPosition(6, 4),
              IntersectionPosition(7, 5)
    ),
    RoadPosition(
              IntersectionPosition(11, 5),
              IntersectionPosition(10, 5)
    ),
    RoadPosition(
              IntersectionPosition(11, 5),
              IntersectionPosition(10, 4)
    ),
    RoadPosition(
              IntersectionPosition(5, 5),
              IntersectionPosition(6, 5)
    ),
    RoadPosition(
              IntersectionPosition(8, 5),
              IntersectionPosition(7, 5)
    ),
    RoadPosition(
              IntersectionPosition(9, 5),
              IntersectionPosition(8, 4)
    ),
    RoadPosition(
              IntersectionPosition(8, 5),
              IntersectionPosition(9, 5)
    ),
    RoadPosition(
              IntersectionPosition(5, 5),
              IntersectionPosition(4, 4)
    ),
    RoadPosition(
              IntersectionPosition(9, 5),
              IntersectionPosition(10, 5)
    ),
    RoadPosition(
              IntersectionPosition(6, 5),
              IntersectionPosition(7, 5)
    ),
}

ALL_NUMBERS = (2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 11, 10, 9, 8, 6, 5, 4, 3)

ALL_RESOURCES = (Resource.BRICK,) * BRICK_TILES + \
                (Resource.DESERT,) * DESERT_TILES + \
                (Resource.LUMBER,) * LUMBER_TILES + \
                (Resource.ORE,) * ORE_TILES + \
                (Resource.WHEAT,) * WHEAT_TILES + \
                (Resource.WOOL,) * WOOL_TILES
