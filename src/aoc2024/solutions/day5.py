from collections import defaultdict
from functools import cmp_to_key
from aoc2024.solution import BaseSolution


class Day5(BaseSolution):
    def __init__(self, raw_input: str):
        super().__init__(raw_input)

        ordering_rules = [line.split("|") for line in self.input if "|" in line]
        updates = [
            [int(update) for update in line.split(",")]
            for line in self.input
            if "," in line
        ]

        self.ordering_rules = [(int(a), int(b)) for (a, b) in ordering_rules]
        self.updates = updates

        to_dependencies = defaultdict(list)
        to_dependents = defaultdict(list)

        for dependency, dependent in self.ordering_rules:
            to_dependencies[dependent].append(dependency)
            to_dependents[dependency].append(dependent)

        self.to_dependencies = to_dependencies
        self.to_dependents = to_dependents

    @classmethod
    def day(cls):
        return 5

    def _is_ordered(self, update: list[int]) -> bool:
        for i in range(len(update)):
            required_before = self.to_dependencies[update[i]]
            required_after = self.to_dependents[update[i]]

            for before in required_before:
                try:
                    idx = update.index(before)
                    if idx > i:
                        return False
                except ValueError:
                    pass

            for after in required_after:
                try:
                    idx = update.index(after)
                    if idx < i:
                        return False
                except ValueError:
                    pass
        return True

    def _sort_within_rules(self, a: int, b: int) -> int:
        if b in self.to_dependents[a]:
            return -1
        if b in self.to_dependencies[a]:
            return 1
        return 0

    def part_1(self):
        middle_sum = 0
        for update in self.updates:
            middle = update[(len(update) - 1) // 2]
            if self._is_ordered(update):
                middle_sum += middle

        return str(middle_sum)

    def part_2(self):
        middle_sum = 0
        for update in self.updates:
            if not self._is_ordered(update):
                ordered = sorted(update, key=cmp_to_key(self._sort_within_rules))
                middle = ordered[(len(ordered) - 1) // 2]
                middle_sum += middle

        return str(middle_sum)
