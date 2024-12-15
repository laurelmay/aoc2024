#!/usr/bin/env bash

if [ -z "$1" ]; then
  >&2 echo "Usage: $0 <DAY>"
  >&2 echo ""
  >&2 echo "A day must be provided"
  exit 1
fi

echo "Initializing Day $1"
file_path="src/aoc2024/solutions/day${1}.py"

if [ -f "$file_path" ]; then
  >&2 echo "Day $1 already exists. Exiting."
  exit 1
fi

cat << EOF > "$file_path"
from aoc2024.solution import BaseSolution


class Day${1}(BaseSolution):
    @classmethod
    def day(cls):
        return ${1}

    def part_1(self):
        return ""

    def part_2(self):
        return ""
EOF
