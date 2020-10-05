"""Author: Dean Quaife
Last Edited: 29/09/2020
Member fields:
m_board: A 2D list representing the 8x8 grid of the board
m_game: The game that this board is a part of"""
class Board:

    """Board constructor: Creates a fresh chessboard for a new game
    game: The game that this board is a part of"""
    def __init__(self, game):
        self.m_board = self._create_board()
        self.m_game = game
        self._place_pieces()

    def move_piece(self, piece, newX, newY):
        if self._is_valid_move(piece, newX, newY) and piece.is_valid_move(newX, newY, self.m_board):
            if self._is_capture(piece, newX, newY):
                self.m_board[newX][newY] = None
            self._set_piece_location(piece, newX, newY)

    """Place each player's pieces on the chessboard"""
    def _place_pieces(self):
        for piece in self.m_game.m_p1.m_pieces:
            x = piece.m_x
            y = piece.m_y
            self.m_board[y][x] = piece

        for piece in self.m_game.m_p2.m_pieces:
            x = piece.m_x
            y = piece.m_y
            self.m_board[y][x] = piece

    """Create the 2D array that will represent the chessboard"""
    @staticmethod
    def _create_board():
        x = []
        for i in range(8):
            x.append(None)
        y = []
        for i in range(8):
            y.append(x.copy())
        return y

    def _is_valid_move(self, piece, newX, newY):
        path = piece.create_path(newX, newY)

        if self._in_bounds(newX, newY) and self._leap_is_valid(piece, path) and self._is_no_ally(piece, newX, newY) and self._not_origin(piece, newX, newY):
            return True

        return False

    """Determines whether the new space is actually on the board"""
    @staticmethod
    def _in_bounds(newX, newY):
        if 0 <= newX < 8 and 0 <= newY < 8:
            return True
        return False

    """Determines whether the new space is different from the current one"""
    @staticmethod
    def _not_origin(piece, newX, newY):
        if piece.m_x != newX or piece.m_y != newY:
            return True
        return False

    """Determines whether the piece can move from its current space to the new one"""
    def _leap_is_valid(self, piece, path):
        #knights can always leap, kings can only ever move one space
        if piece.m_type == "KNIGHT" or piece.m_type == "KING":
            return True

        #pawns can only move one space EXCEPT for their first turn
        if piece.m_type == "PAWN":
            if piece.m_moved:
                return True

        coords = len(path[0])

        for i in range(0,coords):
            if self.m_board[path[0][i]][path[1][i]] is not None:
                return False

        return True

    """Determines whether there is an allied piece in the desired space"""
    def _is_no_ally(self, piece, newX, newY):
        if self.m_board[newX][newY] is None:
            return True
        elif self.m_board[newX][newY] is not None and self.m_board[newX][newY].colour != piece.colour:
            return True
        else:
            return False

    def _is_capture(self, piece, newX, newY):
        if self.m_board[newX][newY] is not None:
            return True
        else:
            return False

    def _set_piece_location(self, piece, newX, newY):
        oldX = piece.m_x
        oldY = piece.m_y

        piece.m_x = newX
        piece.m_y = newY

        self.m_board[newX][newY] = piece
        self.m_board[oldX][oldY] = None