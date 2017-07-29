import random


class ChessKing:
    board = (("H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"),
             ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"),
             ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"),
             ("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"),
             ("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"),
             ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"),
             ("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"),
             ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"))

    def __init__(self, black_king, white_king):
        self.black_king = black_king
        self.white_king = white_king

    def run(self):
        movements = 0
        black_king_adjacent = self.adjacent_cells(self.black_king)

        while self.white_king not in black_king_adjacent:
            movements += 1
            self.white_king = self.next_cell(self.white_king)
        return self.white_king, movements

    @classmethod
    def next_cell(cls, current_cell):
        return random.sample(cls.adjacent_cells(current_cell), 1)[0]

    @classmethod
    def adjacent_cells(cls, position):
        max_limit_h = position[0] == 7
        max_limit_v = position[1] == 7

        left = abs(position[0] - 1)
        right = position[0] + 1 if not max_limit_h else position[0] - 1
        up = abs(position[1] - 1)
        down = position[1] + 1 if not max_limit_v else position[1] - 1

        return {(left, up),
                (left, position[1]),
                (left, down),
                (position[0], up),
                (position[0], down),
                (right, up),
                (right, down),
                (right, position[1])}
