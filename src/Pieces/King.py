"""Author: Dean Quaife
Last Edited: 05/10/2020"""
from src.Pieces.Piece import Piece

class King(Piece):
    """King constructor: Creates a new king
    x, y, player: see Piece.py"""

    def __init__(self, x, y, player):
        super().__init__(x, y, player, "KING")

    def create_path(self, newX, newY):
        return []

    """Check whether a king can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the king can make this move"""

    def is_valid_move(self, newX, newY):
        x_diff = abs(newX, self.m_x)
        y_diff = abs(newY, self.m_y)

        if x_diff < 2 and y_diff < 2:
            return True

        return False