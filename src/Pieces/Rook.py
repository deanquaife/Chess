"""Author: Dean Quaife
Last Edited: 05/10/2020"""
from src.Pieces.Piece import Piece

class Rook(Piece):

    """Rook constructor: Creates a new rook
    Rooks have a field m_moved which indicates whether they have moved yet this game.
    x, y, player: see Piece.py"""
    def __init__(self, x, y, player):
        super().__init__(x, y, player, "ROOK")
        self.m_moved = False

    def create_path(self, newX, newY):
        x_dir = 0
        y_dir = 0

        if newX - self.m_x != 0 and newY == self.m_y: #horizontal move
            pairs = abs(newX - self.m_x)
            if max(newX, self.m_x) == newX:
                x_dir = 1
            else:
                x_dir = -1

        else: #vertical move
            pairs = abs(newY - self.m_y)
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

    """Check whether a rook can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    return: a boolean indicating whether the rook can make this move"""
    def is_valid_move(self, newX, newY):
        if self.m_x == newX or self.m_y == newY:
            return True
        return False