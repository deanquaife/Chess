"""Author: Dean Quaife
Last Edited: 24/09/2020"""
from src.Pieces.Piece import Piece

class Queen(Piece):
    """Queen constructor: Creates a new queen
    x, y, player: see Piece.py"""

    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.m_type = "QUEEN"

    def move(self, newX, newY, board):
        pass

    """Check whether a queen can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the queen can make this move"""

    def is_valid_move(self, newX, newY):
        x_diff = abs(newX, self.m_x)
        y_diff = abs(newY, self.m_y)

        if x_diff == y_diff or newX == self.m_x or newY == self.m_y:
            return True

        return False