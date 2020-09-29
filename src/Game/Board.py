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
