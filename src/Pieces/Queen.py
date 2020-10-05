"""Author: Dean Quaife
Last Edited: 05/10/2020"""
from src.Pieces.Piece import Piece

class Queen(Piece):
    """Queen constructor: Creates a new queen
    x, y, player: see Piece.py"""

    def __init__(self, x, y, player):
        super().__init__(x, y, player, "QUEEN")

    def create_path(self, newX, newY):
        x_dir = 0
        y_dir = 0

        if newY == self.m_y: #horizontal move
            pairs = abs(newX - self.m_x)
            if max(newX, self.m_x) == newX:
                x_dir = 1
            else:
                x_dir = -1

        elif newX == self.m_x: #vertical move
            pairs = abs(newY - self.m_y)
            if max(newY, self.m_y) == newY:
                y_dir = 1
            else:
                y_dir = -1

        else: #diagonal move
            pairs = abs(newX, self.m_x)
            if max(newX, self.m_x) == newX:
                x_dir = 1
            else:
                x_dir = -1
            if max(newY, self.m_y) == newY:
                y_dir = 1
            else:
                y_dir = -1

        path = []
        if pairs - 1 > 0:
            for i in range(0, pairs):
                path[0][i] = newX + x_dir * i
                path[1][i] = newY + y_dir * i

        return path

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