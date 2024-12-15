from itertools import combinations

from aoc2024.solution import BaseSolution


class Day4(BaseSolution):
    def __init__(self, raw_input):
        super().__init__(raw_input)
        self.grid = [list(row) for row in self.input if row]

    @classmethod
    def day(cls):
        return 4

    def _find_in_grid(self, row: int, col: int) -> str:
        if row < 0 or col < 0:
            return "_"
        if row >= len(self.grid) or col >= len(self.grid[0]):
            return "_"
        return self.grid[row][col]

    def part_1(self):
        xmases = 0
        offsets = set(combinations([-1, 0, 1] * 2, 2))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self._find_in_grid(row, col) != "X":
                    continue
                for row_offset, col_offset in offsets:
                    m_location = (row + row_offset * 1, col + col_offset * 1)
                    a_location = (row + row_offset * 2, col + col_offset * 2)
                    s_location = (row + row_offset * 3, col + col_offset * 3)
                    m_candidate = self._find_in_grid(*m_location)
                    a_candidate = self._find_in_grid(*a_location)
                    s_candidate = self._find_in_grid(*s_location)
                    if m_candidate == "M" and a_candidate == "A" and s_candidate == "S":
                        xmases += 1
        return str(xmases)

    def part_2(self):
        xmases = 0
        combos = [("S", "M"), ("M", "S")]
        for row in range(1, len(self.grid) - 1):
            for col in range(1, len(self.grid[0]) - 1):
                if self.grid[row][col] != "A":
                    continue
                up_left = self.grid[row - 1][col - 1]
                up_right = self.grid[row - 1][col + 1]
                down_left = self.grid[row + 1][col - 1]
                down_right = self.grid[row + 1][col + 1]

                if (up_left, down_right) in combos and (up_right, down_left) in combos:
                    xmases += 1

        return str(xmases)
