import pulp # Linear programming tool
from ..game import constants

class LpManager:
    def __init__(self, player):
        self.player = player

        self.roads = list(constants.ALL_ROAD_POSITIONS)
        self.road_choices = pulp.LpVariable.dicts("ROAD_CHOICE", self.roads, cat="Binary")

        self.intersections = list(constants.ALL_INTERSECTION_POSITIONS)
        self.settlement_choices = pulp.LpVariable.dicts("SETTLE_CHOICE", self.intersections, cat="Binary")
        self.city_choices = pulp.LpVariable.dicts("CITY_CHOICE", self.intersections, cat="Binary")

        self.objective_function = pulp.lpSum([
            player.get_road_value(road) * choice_variable
            for road, choice_variable in zip(self.roads, self.road_choices.values())
        ] + [
            player.get_settlement_value(intersection) * choice_variable
            for intersection, choice_variable in zip(self.intersections, self.settlement_choices.values())
        ] + [
            player.get_city_value(intersection) * choice_variable
            for intersection, choice_variable in zip(self.intersections, self.city_choices.values())
        ])

    def get_start_placement(self):
        """
        Return a tuple of (road_placement, settlement_placement)
        """
        #############################################################
        # Get info

        placed_roads = set(self.player.get_roads())
        placed_settlements = set(self.player.get_settlements())
        placed_cities = set(self.player.get_cities())

        blocked_roads = set(self.player.get_blocked_roads())
        blocked_intersections = set(self.player.get_blocked_intersections())

        #############################################################
        # Set up linear programming problem

        problem = pulp.LpProblem("Catan Problem")
        problem += -1 * self.objective_function # Set objective function
        for road in placed_roads:
            problem += (self.road_choices[road] == 0)
        for intersection in placed_settlements:
            problem += (self.settlement_choices[intersection] == 0)
        for intersection in placed_cities:
            problem += (self.settlement_choices[intersection] == 0)
            problem += (self.city_choices[intersection] == 0)

        for road in blocked_roads:
            problem += (self.road_choices[road] == 0)
        for intersection in blocked_intersections:
            problem += (self.settlement_choices[intersection] == 0)
            problem += (self.city_choices[intersection] == 0)

        for intersection in constants.ALL_INTERSECTION_POSITIONS:
            if intersection in blocked_intersections:
                continue
            if intersection not in placed_cities:
                problem += (self.city_choices[intersection] <= self.settlement_choices[intersection])
                if intersection not in placed_settlements:
                    problem += self.settlement_choices[intersection] <= pulp.lpSum([
                        self.road_choices[neighbor_road]
                        for neighbor_road in intersection.get_neighboring_roads()
                    ])

        # Constraints that you place one road and settlement
        problem += (pulp.lpSum(self.road_choices) == 1)
        problem += (pulp.lpSum(self.settlement_choices) == 1)

        ############################################################
        # Solve problem and turn this into a set of moves

        problem.solve(pulp.PULP_CBC_CMD(msg=0))

        road_placement = [road_pos for road_pos, road_choice in
            self.road_choices.items()
            if road_choice.value() > 0.5 and road_pos not in placed_roads][0]

        settlement_placement = [intersection for intersection, settlement_choice in
            self.settlement_choices.items()
            if settlement_choice.value() > 0.5 and intersection not in placed_settlements and
            intersection not in placed_cities][0]

        return (road_placement, settlement_placement)

    def get_turn_placements(self):
        """
        Return a tuple of (road_placements, settlement_placements, city_placements)
        """
        #############################################################
        # Get info

        placed_roads = set(self.player.get_roads())
        placed_settlements = set(self.player.get_settlements())
        placed_cities = set(self.player.get_cities())

        blocked_roads = set(self.player.get_blocked_roads())
        blocked_intersections = set(self.player.get_blocked_intersections())

        #############################################################
        # Set up linear programming problem

        problem = pulp.LpProblem("Catan Problem")
        problem += -1 * self.objective_function # Set objective function
        for road in placed_roads:
            problem += (self.road_choices[road] == 1)
        for intersection in placed_settlements:
            problem += (self.settlement_choices[intersection] == 1)
        for intersection in placed_cities:
            problem += (self.settlement_choices[intersection] == 1)
            problem += (self.city_choices[intersection] == 1)

        for road in blocked_roads:
            problem += (self.road_choices[road] == 0)
        for intersection in blocked_intersections:
            problem += (self.settlement_choices[intersection] == 0)
            problem += (self.city_choices[intersection] == 0)

        for road in constants.ALL_ROAD_POSITIONS:
            if road in placed_roads or road in blocked_roads:
                continue
            problem += (self.road_choices[road] <= pulp.lpSum([
                self.road_choices[neighbor_road]
                for neighbor_road in road.get_neighboring_roads()
            ]))

        for intersection in constants.ALL_INTERSECTION_POSITIONS:
            if intersection in blocked_intersections:
                continue
            if intersection not in placed_cities:
                problem += (self.city_choices[intersection] <= self.settlement_choices[intersection])
                if intersection not in placed_settlements:
                    problem += self.settlement_choices[intersection] <= pulp.lpSum([
                        self.road_choices[neighbor_road]
                        for neighbor_road in intersection.get_neighboring_roads()
                    ])

        ############################
        # Add resource constraints #
        ############################

        # Brick
        problem += (pulp.lpSum(self.road_choices) +
            pulp.lpSum(self.settlement_choices) <=
            self.player.get_brick() + len(placed_roads) + len(placed_settlements) +
            len(placed_cities)
        )
        # Lumber
        problem += (pulp.lpSum(self.road_choices) +
            pulp.lpSum(self.settlement_choices) <=
            self.player.get_lumber() + len(placed_roads) + len(placed_settlements) +
            len(placed_cities)
        )
        # Ore
        problem += (3 * pulp.lpSum(self.city_choices) <=
            self.player.get_ore() + 3 * len(placed_cities)
        )
        # Wheat
        problem += (2 * pulp.lpSum(self.city_choices) + pulp.lpSum(self.settlement_choices) <=
            self.player.get_wheat() + 3 * len(placed_cities) + len(placed_settlements)
        )
        # Wool
        problem += (pulp.lpSum(self.settlement_choices) <=
            self.player.get_wool() + len(placed_settlements) + len(placed_cities)
        )

        ############################################################
        # Solve problem and turn this into a set of moves

        problem.solve(pulp.PULP_CBC_CMD(msg=0))

        road_placements = [road_pos for road_pos, road_choice in
            self.road_choices.items()
            if road_choice.value() > 0.5 and road_pos not in placed_roads]

        settlement_placements = [intersection for intersection, settlement_choice in
            self.settlement_choices.items()
            if settlement_choice.value() > 0.5 and intersection not in placed_settlements and
            intersection not in placed_cities]

        city_placements = [intersection for intersection, settlement_choice in
            self.city_choices.items()
            if settlement_choice.value() > 0.5 and intersection not in placed_roads and
            intersection not in placed_cities]

        return (road_placements, settlement_placements, city_placements)
