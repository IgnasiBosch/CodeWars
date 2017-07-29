"""
###Sudoku Background Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with
digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain
all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

###Sudoku Solution Validator Write a function validSolution that accepts a 2D array representing a Sudoku board, and
returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which
will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

###Examples: validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]])
//Example 1 should return true

validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 0, 3, 4, 8],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]])
//Example 2 should returns false
"""

from itertools import chain
from math import sqrt
from itertools import islice


def valid_solution(board):
    sudoku = Sudoku(board)
    return sudoku.is_valid()


class Sudoku(object):

    """Create a Sudoku object.
    Methods:
        is_valid(): Check if the Sudoku object is valid
    Rules for validation are:
    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3) may also only contain integers: 1..N (N included).
    """
    def __init__(self, matrix=None):
        self.m = None
        self.square_sides = 0
        self.size = 0
        if matrix:
            self.size = len(matrix)
            self.m = matrix
            self.square_sides = int(sqrt(len(matrix)))
        self.nums = {x for x in range(1, len(self.m))}

    def _extract_small_square(self, row, col):
        return [islice(self.m[i], col, self.square_sides + col) for i in range(row, row + self.square_sides)]

    def _check_square(self, row):
        for col in range(0, self.square_sides * 2, self.square_sides):
            square = self._extract_small_square(row, col)
            return self._validate_square(square)

    def _validate_square(self, square):
        sum_square = sum([n for l in square for n in l])
        sum_expected = sum([n for n in range(1, self.size + 1)])
        return sum_square == sum_expected

    def is_valid(self):
        """Validate a Sudoku puzzle of size NxN."""
        for row in self.m:
            if self.nums - set(row): return False #check all rows for valid numbers
        for i in range(len(self.m)): # check all cols for valid numbers
            nums = set()
            for j in range(len(self.m)):
                nums.add(self.m[j][i])
            if self.nums - set(nums): return False
        for l in self.m:        #because True is mask for 1
            for n in l:
                if isinstance(n, bool):
                    return False
        for i in range(0, 1 if self.square_sides == 1 else self.square_sides * 2, self.square_sides):
            try:
                if not self._check_square(i):
                    return False
            except TypeError:
                return False
        return True

def __valid_solution(board):
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        for lst in board:
            if len(set(expected) | set(lst)) != len(expected):
                print(1)
                return False
        for tpl in zip(*board):
            if len(set(expected) | set(tpl)) != len(expected):
                print(2)
                return False

        groups11 = []
        groups12 = []
        groups13 = []
        groups21 = []
        groups22 = []
        groups23 = []
        groups31 = []
        groups32 = []
        groups33 = []
        for row in board[0:3]:
            groups11.append(row[0:3])
            groups21.append(row[3:6])
            groups31.append(row[6:])

        for row in board[3:6]:
            groups12.append(row[0:3])
            groups22.append(row[3:6])
            groups32.append(row[6:])

        for row in board[6:]:
            groups13.append(row[0:3])
            groups23.append(row[3:6])
            groups33.append(row[6:])

        groups = [list(chain.from_iterable(groups11)),
                  list(chain.from_iterable(groups12)),
                  list(chain.from_iterable(groups13)),
                  list(chain.from_iterable(groups21)),
                  list(chain.from_iterable(groups22)),
                  list(chain.from_iterable(groups23)),
                  list(chain.from_iterable(groups31)),
                  list(chain.from_iterable(groups32)),
                  list(chain.from_iterable(groups33))
                  ]

        for lst in groups:
            if len(set(expected) | set(lst)) != len(expected):
                print(3)
                return False
    except:
        return False
    else:
        return True
