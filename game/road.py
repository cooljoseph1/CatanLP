class Road:
    def __init__(self, board, position, owner=None):
        self.board = board
        self.position = position
        self.owner = owner

    def set_owner(self, owner):
        self.owner = owner
