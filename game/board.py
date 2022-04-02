import random
from . import constants
from .tile import Tile
from .intersection import Intersection
from .road import Road
from .resource import Resource

class Board:
    def __init__(self):
        """
        Create a Settlers of Catan board.

        tiles:  A dictionary of (position[], Tile) pairs.
                If None, this is randomly created according
                to `constants.py`.
        """
        #######################################################################
        # Set up tiles
        self.tiles = {} # dictionary of (TilePosition, Tile) pairs

        positions = list(constants.ALL_TILE_POSITIONS)
        random.shuffle(positions)

        for position in positions:
            self.tiles[position] = Tile(self, position)


        resources = list(constants.ALL_RESOURCES)
        random.shuffle(resources)

        numbers = list(constants.ALL_NUMBERS)
        random.shuffle(numbers)

        for position, resource in zip(positions, resources):
            self.tiles[position].set_resource(resource)

        positions_copy = list(positions)
        for number in numbers:
            position = positions_copy.pop()
            if self.tiles[position].resource == Resource.DESERT:
                position = positions_copy.pop()
            self.tiles[position].set_number(number)
        #######################################################################


        #######################################################################
        # Set up intersections
        self.intersections = {
            position: Intersection(self, position)
            for position in constants.ALL_INTERSECTION_POSITIONS
        }
        #######################################################################


        #######################################################################
        # Set up roads
        self.roads = {
            position: Road(self, position)
            for position in constants.ALL_ROAD_POSITIONS
        }
        #######################################################################

    def get_neighboring_tiles(self, intersection_position):
        """
        Return the tile objects of the tiles neighboring a position
        """
        tile_positions = intersection_position.get_neighboring_tiles()
        return [self.tiles[tile_position] for tile_position in tile_positions]

    def get_player_roads(self, player_name):
        """
        Get the road positions owned by `player_name`
        """
        return [road_position for road_position, road in self.roads.items() if road.owner == player_name]

    def get_player_roads_blocked(self, player_name):
        """
        Get the road positions prohibited from `player_name`
        """
        return [road_position for road_position, road in self.roads.items()
                if road.owner is not None and road.owner != player_name]

    def get_player_settlements(self, player_name):
        """
        Get the intersections where `player_name` has a settlement
        """
        return [intersection_pos for intersection_pos, inter in self.intersections.items()
                if inter.owner == player_name and inter.number == 1]

    def get_player_cities(self, player_name):
        """
        Get the intersections where `player_name` has a city
        """
        return [intersection_pos for intersection_pos, inter in self.intersections.items()
                if inter.owner == player_name and inter.number == 2]

    def get_player_intersections_blocked(self, player_name):
        """
        Get the intersections where `player_name` is prohibited from building
        """
        return [intersection_pos for intersection_pos, inter in self.intersections.items()
                if inter.owner is not None and inter.owner != player_name]

    def place_road(self, position, player_name):
        """
        Place a road in the given position for the given player
        """
        if self.roads[position].owner is not None:
            raise Exception("Cannot place a road on top of an already existing road")
        self.roads[position].set_owner(player_name)

    def place_settlement(self, position, player_name):
        """
        Place a settlement in the given position for the given player
        """
        if self.intersections[position].owner is not None:
            raise Exception("Cannot place a settlement on top of an already existing settlement or city")
        self.intersections[position].set_owner(player_name)
        self.intersections[position].set_number(1)

    def place_city(self, position, player_name):
        """
        Place a city in the given position for the given player
        """
        if self.intersections[position].owner is not player_name or self.intersections[position].number != 1:
            raise Exception("Cannot place a city on a place you don't already have a settlement")

        self.intersections[position].set_number(2)

    def __str__(self):
        """
        Convert this to a string for printing.
        """
        board_string = [[" " for x in range(62)] for y in range(34)]
        for ip, i in self.intersections.items():
            x, y = ip.get_render_position()
            if i.owner is None:
                board_string[y][x] = "*"
            else:
                c = str(i.owner)[0].upper()
                board_string[y][x] = c
                if i.number == 2:
                    board_string[y][x-1] = c


        for tp, t in self.tiles.items():
            x, y = tp.get_render_position()
            if t.resource is not None:
                for i, s in enumerate(t.resource.value):
                    board_string[y][x + i - len(t.resource.value) // 2] = s
            for i, s in enumerate(str(t.number)):
                board_string[y+1][x+i - len(str(t.number)) // 2] = s

        for rp, r in self.roads.items():
            x, y = rp.get_render_position()
            board_string[y][x] = "-" if r.owner is None else str(r.owner)[0].lower()

        return "\n".join("".join(str(c) for c in line) for line in board_string)
