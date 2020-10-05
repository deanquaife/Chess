"""Author: Dean Quaife
Last Edited: 05/10/2020"""
from src.Pieces.Piece import Piece

class Knight(Piece):

    """Knight constructor: Creates a new knight
    x, y, player: see Piece.py"""
    def __init__(self, x, y, player):
        super().__init__(x, y, player, "KNIGHT")

    def create_path(self, newX, newY):
        return []

    """Check whether a knight can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the knight can make this move"""
    def is_valid_move(self, newX, newY):
        x_diff = abs(newX, self.m_x)
        y_diff = abs(newY, self.m_y)

        if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            return True
        return False