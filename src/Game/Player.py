"""Author: Dean Quaife
Last Edited: 29/09/2020
Member fields:
m_colour: The player's colour (white/black)
m_pieces: The pieces this player has remaining"""
class Player:

    """Player constructor: creates a new player
    colour: WHITE or BLACK
    Note that m_pieces is created empty as this allows for the player to be created first. The
    pieces can then be initialised with the player and can access the player's colour through
    the 'colour' property in Piece"""
    def __init__(self, colour):
        self.m_colour = colour
        self.m_pieces = []

