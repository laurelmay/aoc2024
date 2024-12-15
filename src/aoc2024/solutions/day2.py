from typing import Literal

from aoc2024.solution import BaseSolution

Direction = Literal[0] | Literal[-1] | Literal[1]


def sign(i: int) -> Direction:
    if i == 0:
        return 0
    if i < 0:
        return -1
    return 1


class Day2(BaseSolution):
    @classmethod
    def day(cls):
        return 2

    def _parse_to_grid(self) -> list[list[int]]:
        rows = self.input
        return [[int(col) for col in row.split()] for row in rows]

    def _is_safe_basic(self, row: list[int]) -> bool:
        start_direction = sign(row[0] - row[1])
        return all(
            [
                1 <= abs(a - b) <= 3 and sign(a - b) == start_direction
                for (a, b) in zip(row, row[1:])
            ]
        )

    def part_1(self) -> str:
        grid = self._parse_to_grid()
        safe_rows = sum([int(self._is_safe_basic(row)) for row in grid])
        return str(safe_rows)

    def _is_safe_step(self, direction: Direction, a: int, b: int) -> bool:
        return (1 <= abs(a - b) <= 3) and sign(a - b) == direction

    def _is_safe_skips(self, row: list[int]) -> bool:
        if self._is_safe_basic(row):
            return True
        # Brute force to try removing each element in the list to see if it's
        # a safe report
        for i in range(0, len(row)):
            adjusted_row = [col for idx, col in enumerate(row) if idx != i]
            if self._is_safe_basic(adjusted_row):
                return True
        return False

    def part_2(self) -> str:
        grid = self._parse_to_grid()
        safe_rows = sum([int(self._is_safe_skips(row)) for row in grid])
        return str(safe_rows)
