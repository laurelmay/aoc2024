import abc


class BaseSolution(abc.ABC):
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.input = raw_input.splitlines()

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
