from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    @abstractmethod
    def can_move(self, position):
        """All pieces must implement to determine if it can move to a chosen
        square, that is if a chosen square is within a piece's movement range
        and is not obstructed by any pieces (unless the piece on a square is
        an enemy piece)"""
        pass


class King(Piece):
    pass


class Queen(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):


class Bishop(Piece):


class Pawn(Piece):
