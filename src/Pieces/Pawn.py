"""Author: Dean Quaife
Last Edited: 24/09/2020"""
from src.Pieces.Piece import Piece

class Pawn(Piece):

    """Pawn constructor: Creates a new pawn
    Pawns have a new field m_moved which indicates whether they have moved yet this game.
    x, y, player: see Piece.py"""
    def __init__(self, x, y, player):
        super(x, y, player)
        self.m_type = "PAWN"
        self.m_moved = False

    def move(self, newX, newY, board):
        pass

    """Check whether a pawn can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    board: the chessboard
    return: a boolean indicating whether the pawn can make this move"""
    def is_valid_move(self, newX, newY, board):
        if self._two_forward(self, newX, newY, board):
            return True
        elif self._diagonal(self, newX, newY, board):
            return True
        elif self._one_forward(self, newX, newY, board):
            return True
        else:
            return False

    """Check whether the pawn can move two spaces forward
    If it has not moved yet and there is no piece occupying either space in front of it, it can.
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    board: the chessboard
    return: a boolean indicating whether the pawn can make this move"""
    def _two_forward(self, newX, newY, board):
        abs_y_diff = abs(newY, self.m_y)
        if not self.m_moved and abs_y_diff == 2 and board.tiles[newX][newY] is None:
            if self.colour == "WHITE" and board.tiles[self.m_x][self.m_y + 1] is None:
                return True
            elif self.colour == "BLACK" and board.tiles[self.m_x][self.m_y - 1] is None:
                return True
        return False

    """Check whether the pawn can move diagonally
    If there is an opposing piece in the space we are trying to move to and the pawn is moving forward, it can
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    board: the chessboard
    return: a boolean indicating whether the pawn can make this move"""
    def _diagonal(self, newX, newY, board):
        abs_x_diff = abs(newX, self.m_x)
        abs_y_diff = abs(newY, self.m_y)
        y_diff = newY - self.m_y
        new_space = board.tiles[newX][newY]
        if abs_x_diff == abs_y_diff == 1 and new_space is not None:
            if self.colour == "WHITE" and new_space.colour == "BLACK" and y_diff > 0:
                return True
            elif self.colour == "BLACK" and new_space.colour == "WHITE" and y_diff < 0:
                return True
        return False

    """Check whether the pawn can move forward
    If there is no piece in front of the pawn, it can
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    board: the chessboard
    return: a boolean indicating whether the pawn can make this move"""
    def _one_forward(self, newX, newY, board):
        abs_y_diff = abs(newY, self.m_y)
        y_diff = newY - self.m_y
        if abs_y_diff == 1 and board.tiles[newX][newY] is None and self.m_x == newX:
            if (self.colour == "WHITE" and y_diff > 0) or (self.colour == "BLACK" and y_diff < 0):
                return True
        return False