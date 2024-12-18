from collections import Counter
from typing import Tuple

from aoc2024.solution import BaseSolution


class Day1(BaseSolution):
    @classmethod
    def day(cls):
        return 1

    def _parse_to_lists(self) -> Tuple[list[int], list[int]]:
        first = []
        second = []
        for line in self.input:
            if not line:
                continue
            a, b = line.split()
            first.append(int(a))
            second.append(int(b))
        return (first, second)

    def part_1(self) -> str:
        first, second = self._parse_to_lists()
        total_distance = sum(
            [abs(a - b) for (a, b) in zip(sorted(first), sorted(second))]
        )
        return str(total_distance)

    def part_2(self) -> str:
        first, second = self._parse_to_lists()
        second_counts = Counter(second)
        similarity_score = sum([i * second_counts.get(i, 0) for i in first])
        return str(similarity_score)
