"""Author: Dean Quaife
Last Edited: 24/09/2020"""
from src.Pieces.Piece import Piece

class Rook(Piece):

    """Rook constructor: Creates a new rook
    Rooks have a field m_moved which indicates whether they have moved yet this game.
    x, y, player: see Piece.py"""
    def __init__(self, x, y, player):
        super().__init__(x, y, player)
        self.m_type = "ROOK"
        self.m_moved = False

    def move(self, newX, newY, board):
        pass

    """Check whether a rook can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the rook can make this move"""
    def is_valid_move(self, newX, newY):
        if self.m_x == newX or self.m_y == newY:
            return True
        return False