import random
from ..game import constants

class GameManager:
    def __init__(self, board, players):
        """
        board:  A game.Board object
        players:  A dictionary of (name, player) items
        """
        self.board = board
        self.players = players

    def run_game(self, rounds=20, starting_locations=4, silent=True):
        ###########################################################
        # Do the starting rounds
        player_order = list(self.players)
        for _ in range(starting_locations):
            player_order = player_order[::-1]
            for player_name in player_order:
                self.players[player_name].place_start()


        ####################################################################
        if not silent:
            print(self.board)
        # Play a bunch of rounds
        for _ in range(rounds):
            # Play 20 rounds and then determine the winner by who has the
            # most victory points
            for player in self.players.values():
                self.roll_dice()
                if not silent:
                    print(player.name, "is going")
                    print("They have", player.resources)
                player.run_turn()
                if not silent:
                    print(self.board)
        return self.get_rankings()

    def get_rankings(self):
        """
        Return a list of the player names so that the top player is positioned
        last.
        """
        ordered_players = sorted(self.players,
            key=lambda player:self.players[player].get_victory_points())
        return {
            player: ordered_players.index(player)
            for player in ordered_players
        }

    def roll_dice(self):
        """
        Roll the dice & give players resources accordingly
        """
        die_roll = random.randrange(1, 7) + random.randrange(1, 7)
        for tile_position, tile in self.board.tiles.items():
            if tile.number != die_roll:
                continue
            for int_pos in tile_position.get_neighboring_intersections():
                intersection = self.board.intersections[int_pos]
                if intersection.owner is None:
                    continue
                self.players[intersection.owner].add_resource(tile.resource, intersection.number)
