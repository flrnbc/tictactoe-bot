"""
Implementation of a tictactoe board. One novelty (following an idea used for Go
boards) is to use 'TStrings' which represent horizontally, vertically or
diagonally connected stones of each player.
Main reference for Go boards: 'Deep learning and Game of Go'.
"""

import enum
from collections import namedtuple

class Player(enum.Enum):
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return[
            Point(self.row - 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row + 1, self.col),
            Point(self.row, self.col + 1),
            Point(self.row + 1, self.col + 1),
            Point(self.row + 1, self.col - 1),
            Point(self.row - 1, self.col + 1),
            Point(self.row - 1, self.col - 1)
        ]


class TString():
    '''
    a TString (standing for tictactoe-string) is the collection of
    diagonally, horizontally or vertically connected stones of one player
    '''
    def __init__(self, color, stones, liberties, orientation):
        # TODO: add the orientation, i.e. horizontal, of a t_string?
        # i think this would make it easier to merge t_strings correctly
        self.color = color
        self.stones = set(stones)
        # TODO: do we need liberties of single points as well?
        # at least not for the game mechanic but i wonder about a neural network
        # so that it can "see" the liberties of a single stone (to start a longer t_string)
        self.liberties = set(liberties)
        self.orientation = orientation

    def __len__(self):
        return len(self.stones)

    def merged_with(self, t_string):
        assert t_string.color == self.color
        assert t_string.orientation == self.orientation
        combined_stones = self.stones | t_string.stones
        return TString(
            self.color,
            combined_stones,
            (self.liberties | t_string.liberties) - combined_stones,
            orientation)


class TBoard():
    '''tictactoe-board of arbitrary size; including number of stones that have to be connected'''
    def __init__(self, num_cols, num_rows, connect_stones):
        # connect_stones: number of stones that need to be connected
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.connect_stones = connect_stones
        # {key = point : value = {key = orientation : value = t_strings (of all orientations) passing through point}}
        self._grid = {}

    def place_stone(self, player, point):
        '''place a stone at the given point on the board'''
        # NOTE: i think here we diverge from Go the most because
        # we merge t_strings and hence liberties differently (only
        # horizontal, diagonal, vertical ones)
        pass

    def is_on_board(self, point):
        '''check if point is on board'''
        return 1 <= point.row <= self.num_rows and \
            1 <= point.col <= self.num_cols

    def get(self, point):
        '''get the color of the point'''
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color

    def get_t_strings(self, point):
        t_strings_dict = self._grid.get(point)
        if string is None:
            return None
        return t_strings_dict


# NEXT:
# class TGameState():
