import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution03(Solution):
    def part1(self) -> int:
        total = 0
        for bank in self.input_data:
            voltage = self.get_voltage_with_two_digits(bank)
            total += int(voltage)
        return total

    def part2(self) -> int:
        total = 0
        for bank in self.input_data:
            voltage = self.get_voltage_with_twelve_digits(bank)
            total += int(voltage)
        return total

    def get_voltage_with_two_digits(self, bank):
        max_1 = (-1, -1)
        max_2 = (-1, -1)
        for idx, battery in enumerate(bank[:-1]):
            if int(battery) > int(max_1[0]):
                max_1 = (battery, idx)

        start = max_1[1] + 1
        for idx in range(start, len(bank)):
            battery = bank[idx]
            if int(battery) > int(max_2[0]):
                max_2 = (battery, idx)

        return int(str(max_1[0]) + str(max_2[0]))

    def get_voltage_with_twelve_digits(self, bank):
        digits = 12
        batteries = []
        start = 0

        for _ in range(digits):
            remaining = digits - len(batteries) - 1
            end = len(bank) - remaining

            max_digit = (-1, -1)

            for idx in range(start, end):
                battery = bank[idx]
                if int(battery) > int(max_digit[0]):
                    max_digit = (battery, idx)

            batteries.append(str(max_digit[0]))

            start = max_digit[1] + 1

        return int("".join(batteries))
