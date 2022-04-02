class Tile:
    def __init__(self, board, position, resource=None, number=-1):
        """
        Create a board tile.

        resource:  None is the default and means desert
        number:  -1 is the default and will never be rolled (i.e. desert)
        """
        self.board = board
        self.position = position
        self.resource = resource
        self.number = number

    def set_resource(self, resource):
        self.resource = resource

    def set_number(self, number):
        self.number = number

    def get_probability(self):
        if self.number < 2 or self.number > 12:
            return 0.0
        return min(self.number - 1, 13 - self.number) / 36.0
