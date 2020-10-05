"""Author: Dean Quaife
Last Edited: 05/10/2020"""
from src.Pieces.Piece import Piece

class Bishop(Piece):
    """Bishop constructor: Creates a new bishop
    x, y, player: see Piece.py"""

    def __init__(self, x, y, player):
        super().__init__(x, y, player, "BISHOP")

    def create_path(self, newX, newY):
        pairs = abs(newX, self.m_x)

        x_dir = 1
        y_dir = 1
        if newX - self.m_x < 0:
            x_dir = -1
        if newY - self.m_y < 0:
            y_dir = -1

        path = []
        if pairs - 1 > 0:
            for i in range(0, pairs):
                path[0][i] = newX + x_dir * i
                path[1][i] = newY + y_dir * i

        return path

    """Check whether a bishop can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the bishop can make this move"""

    def is_valid_move(self, newX, newY):
        x_diff = abs(newX, self.m_x)
        y_diff = abs(newY, self.m_y)

        return x_diff == y_diff