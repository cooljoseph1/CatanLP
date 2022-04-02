from ..game import Resource
from .lp_manager import LpManager

class Player:
    def __init__(self, board, name, cost_manager):
        self.board = board
        self.name = name
        self.cost_manager = cost_manager

        self.lp_manager = LpManager(self)

        self.resources = {
            Resource.BRICK: 0,
            Resource.LUMBER: 0,
            Resource.ORE: 0,
            Resource.WHEAT: 0,
            Resource.WOOL: 0,
        }

    ##############################################################

    def get_roads(self):
        """
        Return a list of the road positions we have
        """
        return self.board.get_player_roads(self.name)

    def get_blocked_roads(self):
        """
        Return a list of the road positions other people have blocked
        """
        return self.board.get_player_roads_blocked(self.name)

    def get_settlements(self):
        return self.board.get_player_settlements(self.name)

    def get_cities(self):
        return self.board.get_player_cities(self.name)

    def get_blocked_intersections(self):
        return self.board.get_player_intersections_blocked(self.name)

    #################################################################

    def get_victory_points(self):
        return len(self.get_settlements()) + 2 * len(self.get_cities())

    #################################################################

    def get_resource_amount(self, resource):
        return self.resources[resource]

    def get_brick(self):
        return self.resources[Resource.BRICK]

    def get_lumber(self):
        return self.resources[Resource.LUMBER]

    def get_ore(self):
        return self.resources[Resource.ORE]

    def get_wheat(self):
        return self.resources[Resource.WHEAT]

    def get_wool(self):
        return self.resources[Resource.WOOL]

    def add_resource(self, resource, amount=1):
        self.resources[resource] += amount

    def subtract_resource(self, resource, amount=1):
        if amount > self.resources[resource]:
            raise ValueError("Cannot subtract that many resources.")

        self.resources[resource] -= amount

    ##################################################################


    def get_road_value(self, road_position):
        return self.cost_manager.get_road_value(road_position)

    def get_settlement_value(self, intersection_position):
        return self.cost_manager.get_settlement_value(intersection_position)

    def get_city_value(self, intersection_position):
        return self.cost_manager.get_city_value(intersection_position)

    ##################################################################

    def run_turn(self):
        road_placements, settlement_placements, city_placements = self.lp_manager.get_turn_placements()
        for road in road_placements:
            self.subtract_resource(Resource.BRICK)
            self.subtract_resource(Resource.LUMBER)
            self.board.place_road(road, self.name)

        for settlement in settlement_placements:
            self.subtract_resource(Resource.BRICK)
            self.subtract_resource(Resource.LUMBER)
            self.subtract_resource(Resource.WHEAT)
            self.subtract_resource(Resource.WOOL)
            self.board.place_settlement(settlement, self.name)

        for city in city_placements:
            self.subtract_resource(Resource.ORE, 3)
            self.subtract_resource(Resource.WHEAT, 2)
            self.board.place_city(city, self.name)

    def place_start(self):
        """
        Place down a single road and settlement anywhere
        """
        road_placement, settlement_placement = self.lp_manager.get_start_placement()
        self.board.place_road(road_placement, self.name)
        self.board.place_settlement(settlement_placement, self.name)
