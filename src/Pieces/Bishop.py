"""Author: Dean Quaife
Last Edited: 24/09/2020"""
from src.Pieces.Piece import Piece

class Bishop(Piece):
    """Bishop constructor: Creates a new bishop
    x, y, player: see Piece.py"""

    def __init__(self, x, y, player):
        super(x, y, player)
        self.m_type = "BISHOP"

    def move(self, newX, newY, board):
        pass

    """Check whether a bishop can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the bishop can make this move"""

    def is_valid_move(self, newX, newY):
        x_diff = abs(newX, self.m_x)
        y_diff = abs(newY, self.m_y)

        return x_diff == y_diff