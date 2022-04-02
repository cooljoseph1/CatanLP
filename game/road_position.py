class RoadPosition:
    def __init__(self, intersection1, intersection2):
        self.intersections = frozenset({intersection1, intersection2})

    def __hash__(self):
        return hash(("Road Position", self.intersections))

    def __eq__(self, other):
        return type(self) == type(other) and self.intersections == other.intersections

    def __repr__(self):
        return f"RoadPosition({str(self.intersections)})"

    def get_neighboring_intersections(self):
        return set(self.intersections)

    def get_neighboring_roads(self):
        roads = set()
        for intersection in self.intersections:
            roads |= intersection.get_neighboring_roads()
        roads.remove(self)
        return roads

    def is_next_to(self, other):
        return len(self.intersections & other.intersections) == 1

    def is_next_to_intersection(self, intersectionPosition):
        return intersectionPosition in self.intersections

    def get_render_position(self):
        ints = list(self.intersections)
        r1 = ints[0].get_render_position()
        r2 = ints[1].get_render_position()
        return ((r1[0] + r2[0]) // 2, (r1[1] + r2[1]) // 2)
