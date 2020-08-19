from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def __init__(self, x, y, player):
        self.m_x = x
        self.m_y = y
        self.m_player = player

    @abstractmethod
    def move(self, newX, newY, board):
        pass

    @abstractmethod
    def is_valid_move(self, newX, newY, board):
        pass

    @property
    def colour(self):
        return self.m_player.colour