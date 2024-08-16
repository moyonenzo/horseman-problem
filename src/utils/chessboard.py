from typing import final, Union
from dataclasses import dataclass


@dataclass(frozen=True)
class PathItem:
    x: int
    y: int


class Chessboard:
    def __init__(self, size: int = 8):
        self.__size = size
        self.__board = [[False]*size]*size

    @final
    def get_possible_moves_for_position(self, x: int, y: int) -> list[PathItem]:
        __moves = [
            PathItem(x - 2, y - 1),
            PathItem(x - 1, y - 2),
            PathItem(x + 2, y - 1),
            PathItem(x + 1, y - 2),
            PathItem(x - 2, y + 1),
            PathItem(x - 1, y + 2),
            PathItem(x + 2, y + 1),
            PathItem(x + 1, y + 2)
        ]

        moves = []
        for move in __moves:
            if move.x != x and move.y != y:
                if 0 <= move.x < self.__size and 0 <= move.y < self.__size:
                    moves.append(move)

        return moves

    @final
    def is_in_path(self, path, x, y) -> bool:
        return any(PathItem(x, y) == path_item for path_item in path)

    @final
    def solve(self, x: int, y: int) -> Union[list[PathItem], None]:
        path = [PathItem(x=x, y=y)]
        path_tried = {}

        while len(path) < self.__size**2:
            try:
                position = path[-1]
            except IndexError:
                return None

            if position not in path_tried:
                path_tried[position] = []

            moves = self.get_possible_moves_for_position(position.x, position.y)
            moves = list(filter(lambda move: not self.is_in_path(path, move.x, move.y), moves))
            moves = list(filter(lambda move: move not in path_tried[position], moves))

            if len(moves) == 0:
                del path_tried[path.pop()]
                continue

            path_tried[position].append(moves[0])
            path.append(moves[0])

        return path
