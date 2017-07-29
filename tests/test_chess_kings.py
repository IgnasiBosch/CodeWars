from unittest import TestCase
from src.chess_kings import ChessKing


class TestChessKings(TestCase):

    def test_adjacent_cells_1(self):
        position = (0, 1)
        adjacent = ChessKing.adjacent_cells(position)
        expected = {(1, 2), (0, 2), (1, 0), (0, 0), (1, 1)}

        self.assertSetEqual(expected, adjacent)

    def test_adjacent_cells_2(self):
        position = (7, 7)
        adjacent = ChessKing.adjacent_cells(position)
        expected = {(7, 6), (6, 6), (6, 7)}

        self.assertSetEqual(expected, adjacent)

    def test_adjacent_cells_3(self):
        position = (4, 3)
        adjacent = ChessKing.adjacent_cells(position)
        expected = {(5, 4), (3, 2), (3, 3), (4, 4), (5, 2), (4, 2), (3, 4), (5, 3)}

        self.assertSetEqual(expected, adjacent)

    # def test_1(self):
    #     white_king = (2, 3)
    #     black_king = (5, 5)
    #
    #
    #     self.assertTrue(valid_solution(matrix))
