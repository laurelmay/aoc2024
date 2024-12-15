import importlib.util
import inspect
import os
import types
from typing import Dict, Type

from aoc2024 import solution

_SOLUTIONS = {}
_LOADED = False

SolutionType = Type[solution.BaseSolution]


def _is_subclass(sub, parent) -> bool:
    return inspect.isclass(sub) and issubclass(sub, parent)


def _is_ignored(solution: SolutionType) -> bool:
    return solution.ignored()


def _declared_in_module(module: types.ModuleType) -> list[str]:
    dict_items = [item for item in module.__dict__.keys() if not item.startswith("__")]
    return [
        item_name
        for item_name in dict_items
        if not isinstance(item := getattr(module, item_name), types.ModuleType)
        and item.__module__ == module.__name__
    ]


def _load_solutions(directory: str | None = None) -> Dict[str, SolutionType]:
    if not directory:
        directory = os.path.dirname(os.path.realpath(__file__))
    modules = {
        filename
        for filename in os.listdir(directory)
        if filename.endswith(".py") and filename != "__init__.py"
    }

    solutions = {}

    for module in modules:
        module_path = os.path.join(directory, module)
        module_name = os.path.splitext(module)[0]

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if not spec or not spec.loader:
            continue
        solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(solution_module)

        module_contents = [
            getattr(solution_module, module_item)
            for module_item in _declared_in_module(solution_module)
        ]

        solutions_in_module = {
            str(solution_class.day()): solution_class
            for solution_class in module_contents
            if _is_subclass(solution_class, solution.BaseSolution)
            and not _is_ignored(solution_class)
        }

        solutions.update(solutions_in_module)

    return solutions


if not _LOADED:
    _SOLUTIONS = _load_solutions()


def all_solutions() -> Dict[str, SolutionType]:
    return dict(_SOLUTIONS)
