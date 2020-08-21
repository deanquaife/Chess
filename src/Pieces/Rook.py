"""Author: Dean Quaife
Last Edited: 21/08/2020"""
from src.Pieces.Piece import Piece

class Rook(Piece):

    """Rook constructor: Creates a new rook
    Rooks have a new field m_moved which indicates whether they have moved yet this game.
    x, y, player: see Piece.py"""
    def __init__(self, x, y, player):
        super(x, y, player)
        self.m_type = "ROOK"
        self.m_moved = False

    def move(self, newX, newY, board):
        pass

    """Check whether a rook can make this move
    newX: the X coordinate we're trying to move to
    newY: the Y coordinate we're trying to move to
    board: the chessboard
    return: a boolean indicating whether the rook can make this move"""
    def is_valid_move(self, newX, newY, board):
        if self.m_x == newX: #we're moving vertically
            for y in range(min(self.m_y, newY), max(self.m_y, newY)):
                if board.m_board[self.m_x][y] is not None:
                    return False
        elif self.m_y == newY: #we're moving horizontally
            for x in range(min(self.m_x, newX), max(self.m_x, newX)):
                if board.m_board[x][self.m_y] is not None:
                    return False
        else: #rooks can only move horizontally or vertically!
            return False

        new_space = board.m_board[newX][newY]
        if new_space is not None: #if there's a piece there, is it an enemy one?
            if self.colour == "WHITE" and new_space.colour == "BLACK":
                return True
            elif self.colour == "BLACK" and new_space.colour == "WHITE":
                return True
        return False