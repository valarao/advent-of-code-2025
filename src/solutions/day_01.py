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
        dial = 50

        for rotation_info in self.input_data:
            direction, rotation = self.parse_rotation_info(rotation_info)
            full_turns = rotation // 100
            remainder = rotation % 100

            counts += full_turns
            if self.has_additional_click(remainder, direction, dial):
                counts += 1

            dial = self.update_dial(direction, dial, rotation)

        return counts

    def parse_rotation_info(self, rotation_info):
        return (rotation_info[0], int(rotation_info[1:]))

    def has_additional_click(self, remainder, direction, dial):
        if remainder == 0:
            return False

        if direction == "L":
            distance_to_zero = dial
        else:
            distance_to_zero = 100 - dial

        return remainder >= distance_to_zero and distance_to_zero > 0

    def update_dial(self, direction, dial, rotation):
        if direction == "L":
            return (dial - rotation) % 100
        else:
            return (dial + rotation) % 100
