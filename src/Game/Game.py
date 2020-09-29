"""Author: Dean Quaife
Last Edited: 29/09/2020
Member fields:
m_board: The chessboard associated with this game
m_p1: Player one (white side)
m_p2: Player two (black side)"""
from src.Pieces.Pawn import Pawn
from src.Pieces.Rook import Rook
from src.Pieces.Bishop import Bishop
from src.Pieces.Knight import Knight
from src.Pieces.Queen import Queen
from src.Pieces.King import King
from src.Game.Board import Board
from src.Game.Player import Player

class Game:

    """Game constructor: Creates a new game session"""
    def __init__(self):
        self.m_p1 = Player("WHITE")
        self.m_p2 = Player("BLACK")
        self._create_pieces_p1()
        self._create_pieces_p2()
        self.m_board = Board(self)

    """Initialise the pieces for player 1"""
    def _create_pieces_p1(self):
        for i in range(0, 8):
            self.m_p1.m_pieces.append(Pawn(i, 6, self.m_p1))

        self.m_p1.m_pieces.append(Rook(0, 7, self.m_p1))
        self.m_p1.m_pieces.append(Rook(7, 7, self.m_p1))

        self.m_p1.m_pieces.append(Knight(1, 7, self.m_p1))
        self.m_p1.m_pieces.append(Knight(6, 7, self.m_p1))

        self.m_p1.m_pieces.append(Bishop(2, 7, self.m_p1))
        self.m_p1.m_pieces.append(Bishop(5, 7, self.m_p1))

        self.m_p1.m_pieces.append(Queen(3, 7, self.m_p1))

        self.m_p1.m_pieces.append(King(4, 7, self.m_p1))

    """Initialise the pieces for player 2"""
    def _create_pieces_p2(self):
        for i in range(0, 8):
            self.m_p2.m_pieces.append(Pawn(i, 1, self.m_p2))

        self.m_p2.m_pieces.append(Rook(0, 0, self.m_p2))
        self.m_p2.m_pieces.append(Rook(7, 0, self.m_p2))

        self.m_p2.m_pieces.append(Knight(1, 0, self.m_p2))
        self.m_p2.m_pieces.append(Knight(6, 0, self.m_p2))

        self.m_p2.m_pieces.append(Bishop(2, 0, self.m_p2))
        self.m_p2.m_pieces.append(Bishop(5, 0, self.m_p2))

        self.m_p2.m_pieces.append(Queen(3, 0, self.m_p2))

        self.m_p2.m_pieces.append(King(4, 0, self.m_p2))