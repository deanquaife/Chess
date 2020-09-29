"""Author: Dean Quaife
Last Edited: 29/09/2020
Member fields:
m_x: The x coordinate of this piece
m_y: The y coordinate of this piece
m_player: The player who owns this piece"""
from abc import ABC, abstractmethod

class Piece(ABC):

    """Piece constructor: Creates a new piece
    x: The piece's starting x coordinate
    y: The piece's starting y coordinate
    player: The player who owns this piece
    All of these will be passed in during the creation of a Game"""
    @abstractmethod
    def __init__(self, x, y, player):
        self.m_x = x
        self.m_y = y
        self.m_player = player

    """Move the piece to [newX,newY] on the board"""
    @abstractmethod
    def move(self, newX, newY, board):
        pass

    """Determines whether the piece can move to [newX,newY] this turn"""
    @abstractmethod
    def is_valid_move(self, newX, newY, board):
        pass

    """Ease of use"""
    @property
    def colour(self):
        return self.m_player.m_colour