import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution01(Solution):
    def part1(self) -> int:
        counts = 0
        dial_number = 50

        for x in self.input_data:
            if x[0] == "L":
                dial_number = (dial_number - int(x[1:])) % 100
            else:
                dial_number = (dial_number + int(x[1:])) % 100
            if dial_number == 0:
                counts += 1

        return counts

    def part2(self) -> int:
        counts = 0
        dial_number = 50

        for x in self.input_data:
            direction = x[0]
            rotation = int(x[1:])

            if direction == "L":
                counts += rotation // 100
                remainder = rotation % 100
                if dial_number > 0 and remainder >= dial_number:
                    counts += 1
                dial_number = (dial_number - rotation) % 100
            else:
                counts += rotation // 100
                remainder = rotation % 100
                if remainder > 0 and remainder >= (100 - dial_number):
                    counts += 1
                dial_number = (dial_number + rotation) % 100

        return counts
