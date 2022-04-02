import random
import json
from ..game import constants, Board, Resource
from ..game_manager import GameManager, Player, CostManager

class Genome:
    def __init__(self, income_values=None, resource_values=None,
            road_value=None, settlement_value=None, city_value=None):

        if income_values is None:
            # Create random income values
            income_values = {
                resource: random.random()  * 100
                for resource in constants.ALL_RESOURCE_TYPES
            }
        self.income_values = income_values

        if resource_values is None:
            # Create random income values
            resource_values = {
                resource: random.random()  * 10
                for resource in constants.ALL_RESOURCE_TYPES
            }
        self.resource_values = resource_values
        self.road_value = random.random() * 20 if road_value is None else road_value
        self.settlement_value = random.random() * 20 if settlement_value is None else settlement_value
        self.city_value = random.random() * 20 if city_value is None else city_value

    def cross(self, other):
        """
        Return a new genome that is the crossing over of this and another genome
        """
        income_values = {
            resource: (self.income_values[resource] + other.income_values[other]) / 2
            for resource in self.income_values
        }
        resource_values = {
            resource: (self.income_values[resource] + other.income_values[other]) / 2
            for resource in self.resource_values
        }
        road_value = (self.road_value + other.road_value) / 2
        settlement_value = (self.settlement_value + other.settlement_value) / 2
        city_value = (self.city_value + other.city_value) / 2
        return Genome(income_values, resource_values, road_value, settlement_value, city_value)

    def mutate(self):
        """
        Return a mutated version of ourself.
        """
        pass

    def __str__(self):
        return str(
            {
                "income_values": self.income_values,
                "resource_values": self.resource_values,
                "road_value": self.road_value,
                "settlement_value": self.settlement_value,
                "city_value": self.city_value,
            }
        )

    @staticmethod
    def compare(*genomes, num_games=5):
        """
        Test up to 4 genomes against each other
        """
        genomes = list(genomes)
        sum_ranks = [0 for genome in genomes]
        name_indexes = {"ABCD"[i]: i for i, genome in enumerate(genomes)}
        genome_names = {"ABCD"[i]: genome for i, genome in enumerate(genomes)}

        for _ in range(num_games):
            board = Board()
            random.shuffle(genomes)
            cost_managers = {
                name: CostManager(
                    board,
                    genome.income_values,
                    genome.resource_values,
                    genome.road_value,
                    genome.settlement_value,
                    genome.city_value
                ) for name, genome in genome_names.items()
            }

            players = {
                name: Player(board, name, cost_manager)
                for name, cost_manager in cost_managers.items()
            }

            game_manager = GameManager(board, players)
            ranks = game_manager.run_game()
            for name, ranking in ranks.items():
                sum_ranks[name_indexes[name]] += ranking
        return sum_ranks
