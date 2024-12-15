import abc


def clean_input_lines(lines: list[str]) -> list[str]:
    start = 0
    end = -1
    if not lines[0]:
        start += 1
    if not lines[-1]:
        end -= 2
    return lines[start:end]


class BaseSolution(abc.ABC):
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.input = clean_input_lines(raw_input.splitlines())

    @classmethod
    def ignored(cls) -> bool:
        return False

    @classmethod
    @abc.abstractmethod
    def day(cls) -> int:
        pass

    @abc.abstractmethod
    def part_1(self) -> str:
        pass

    @abc.abstractmethod
    def part_2(self) -> str:
        pass
