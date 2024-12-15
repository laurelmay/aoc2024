import typing

import click

from .solutions import all_solutions

_SOLUTIONS = all_solutions()


def available_days() -> list[str]:
    return sorted([str(key) for key in _SOLUTIONS.keys()])


@click.command("aoc2024")
@click.option("-i", "--input-file", type=click.File("r"), required=True)
@click.option("-o", "--output-file", type=click.File("w"), default="-")
@click.option("-d", "--day", type=click.Choice(available_days()), required=True)
def cli(input_file: typing.IO, output_file: typing.IO, day: str):
    SolverCls = _SOLUTIONS[day]

    solver = SolverCls(input_file.read())

    if part_1 := solver.part_1():
        print(f"Part 1: {part_1}", file=output_file)

    if part_2 := solver.part_2():
        print(f"Part 2: {part_2}", file=output_file)
