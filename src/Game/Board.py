"""Author: Dean Quaife
Last Edited: 19/08/2020
Member fields for the Board class:
m_board: A 2D list representing the 8x8 grid of the board
m_p1: The player moving first (white-side)
m_p2: The player moving second(black-side)"""
class Board:

    """Board constructor: Creates a fresh chessboard for a new game
    player_one: The player moving first
    player_two: The player moving second"""
    def __init__(self, player_one, player_two):
        x = []
        for i in range(8):
            x.append(None)
        y = []
        for i in range(8):
            y.append(x)

        self.m_board = y
        self.m_p1 = player_one
        self.m_p2 = player_two
        self._place_pieces()

    """Place each player's pieces on the chessboard"""
    def _place_pieces(self):
        iterator = iter(self.m_p1.pieces)
        for i in range(2):
            for j in range(8):
                    self.m_board[i][j] = next(iterator)

        iterator = iter(self.m_p2.pieces)
        for i in range(7, 5, -1):
            for j in range(8):
                self.m_board[i][j] = next(iterator)