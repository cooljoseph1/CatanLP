from ..game import constants
from ..game import Resource

class CostManager:
    def __init__(self, board, incomes_value, resources_value, road_value,
            settlement_value, city_value):
        self.board = board

        self.incomes_value = incomes_value
        self.resources_value = resources_value
        self.road_value = road_value
        self.settlement_value = settlement_value
        self.city_value = city_value

    def get_road_value(self, road_position):
        value = self.road_value - self.resources_value[Resource.BRICK] - self.resources_value[Resource.LUMBER]
        return value

    def get_settlement_value(self, intersection_position):
        build_cost = sum(
            self.resources_value[resource]
            for resource in [Resource.BRICK, Resource.LUMBER, Resource.WHEAT, Resource.WOOL]
        )
        income_value = sum(
            self.incomes_value[tile.resource] * tile.get_probability()
            for tile in self.board.get_neighboring_tiles(intersection_position)
            if tile.resource != Resource.DESERT
        )
        return self.settlement_value + income_value - build_cost

    def get_city_value(self, intersection_position):
        build_cost = sum(
            self.resources_value[resource]
            for resource in [Resource.ORE, Resource.ORE, Resource.ORE, Resource.WHEAT, Resource.WHEAT]
        )
        income_value = sum(
            self.incomes_value[tile.resource] * tile.get_probability()
            for tile in self.board.get_neighboring_tiles(intersection_position)
            if tile.resource != Resource.DESERT
        )
        return self.city_value + income_value - build_cost
