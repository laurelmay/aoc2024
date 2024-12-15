# aoc2024

Advent of Code 2024 (partially) completed in Python.

## Prerequisites

To run the solutions you will need to have [PDM installed][pdm-install]. This is
the Python package manager used by this project.

[pdm-install]: https://pdm-project.org/en/latest/#installation

## Organization

The solutions themselves are in the `src/aoc2024/solutions/` folder named
by the day of the puzzle. The first part of the puzzle is implemented in a
method called `part_1` and the second part of the puzzle is implemented in
a method called `part_2`. These will automatically be called by the CLI (if
implemented) when invoked.

## Running

To run the solutions, you will first need to run `pdm install` to initialize the
project. This is a one-time requirement.

Subsequently, running a particular day's solution can be done by running:

```bash
pdm run aoc2024 <-d DAY> [-i INPUT_FILE]
```

`DAY` should be substituted with the day of December to solve for and `INPUT_FILE`
should be the file with the puzzle input (which defaults to standard input).

For example,

```bash
pdm run aoc2024 -d 2 -i inputs/day2.txt
```
