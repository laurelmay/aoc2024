from aoc2024.solution import BaseSolution


class Day3(BaseSolution):
    @classmethod
    def day(cls):
        return 3

    def _execute_memory_muls(self, with_conditionals=False) -> int:
        corruputed_memory = self.raw_input
        enable_mul = True
        instruction_args = []
        buffer = ""
        pair = ["", ""]
        in_parens = False
        set_position = 0

        def reset():
            nonlocal buffer, pair, in_parens, set_position
            buffer = ""
            pair = ["", ""]
            in_parens = False
            set_position = 0

        def commit():
            nonlocal enable_mul
            if (
                enable_mul
                and buffer == "mul"
                and 1 <= len(pair[0]) <= 3
                and 1 <= len(pair[1]) <= 3
            ):
                instruction_args.append((int(pair[0]), int(pair[1])))
            elif buffer == "do":
                enable_mul = True
            elif buffer == "don't" and with_conditionals:
                enable_mul = False
            reset()

        for c in corruputed_memory:
            match c:
                case "m":
                    reset()
                    buffer = "m"
                case "u" if buffer == "m":
                    buffer += c
                case "l" if buffer == "mu":
                    buffer += c
                case "d":
                    reset()
                    buffer = "d"
                case "o" if buffer == "d":
                    buffer += c
                case "n" if buffer == "do":
                    buffer += c
                case "'" if buffer == "don":
                    buffer += c
                case "t" if buffer == "don'":
                    buffer += c
                case "(" if buffer in ["mul", "do", "don't"] and not in_parens:
                    in_parens = True
                case c if c.isdigit() and buffer == "mul" and in_parens and 0 <= len(
                    pair[set_position]
                ) <= 2:
                    pair[set_position] += c
                case "," if buffer == "mul" and in_parens and set_position == 0:
                    set_position = 1
                case ")" if buffer in ["mul", "do", "don't"] and in_parens:
                    commit()
                case _:
                    reset()
        return sum([a * b for a, b in instruction_args])

    def part_1(self) -> str:
        return str(self._execute_memory_muls())

    def part_2(self) -> str:
        return str(self._execute_memory_muls(with_conditionals=True))
