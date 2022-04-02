class Intersection:
    def __init__(self, board, position, owner=None, number=0):
        """
        Create a board tile.

        owner:  None is the default and means unsettled
        number:  0 for nothing, 1 for settlement, 2 for city
        """
        self.board = board
        self.position = position
        self.owner = owner
        self.number = number

    def set_owner(self, owner):
        self.owner = owner

    def set_number(self, number):
        self.number = number
