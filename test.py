from .game import Board, Resource
from .game_manager import GameManager, Player, CostManager

board = Board()


income_values = {
    Resource.BRICK: 100,
    Resource.LUMBER: 100,
    Resource.ORE: 100,
    Resource.WHEAT: 100,
    Resource.WOOL: 100,
}

resource_values = {
    Resource.BRICK: 1,
    Resource.LUMBER: 1,
    Resource.ORE: 1,
    Resource.WHEAT: 1,
    Resource.WOOL: 1,
}

road_value = 0
settlement_value = 10
city_value = 15

cost_manager = CostManager(board, income_values, resource_values, road_value, settlement_value, city_value)

player1 = Player(board, "Alpha", cost_manager)
player2 = Player(board, "Beta", cost_manager)
player3 = Player(board, "Gamma", cost_manager)

game_manager = GameManager(board, {"Alpha": player1, "Beta": player2, "Gamma": player3})
game_manager.run_game(50, 4, False)
