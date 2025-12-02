import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution02(Solution):
    def part1(self) -> int:
        id_ranges = self.get_id_ranges(self.input_data)

        expanded_ids = []
        for id_range in id_ranges:
            expanded_ids += self.expand_id_range(id_range)

        total = 0
        for id in expanded_ids:
            if self.is_id_invalid_by_twice_repetition(id):
                total += int(id)

        return total

    def part2(self) -> int:
        id_ranges = self.get_id_ranges(self.input_data)

        expanded_ids = []
        for id_range in id_ranges:
            expanded_ids += self.expand_id_range(id_range)

        total = 0
        for id in expanded_ids:
            if self.is_id_invalid_by_n_repetition(id):
                total += int(id)

        return total

    def get_id_ranges(self, raw_input_data):
        all_id_ranges = []
        for id_ranges in raw_input_data:
            for id_range in id_ranges.split(","):
                start_id, end_id = id_range.split("-")
                all_id_ranges.append((int(start_id), int(end_id)))
        return all_id_ranges

    def expand_id_range(self, id_range):
        start_id, end_id = id_range

        expanded_range = []
        for n in range(start_id, end_id + 1):
            expanded_range.append(str(n))

        return expanded_range

    def is_id_invalid_by_twice_repetition(self, id):
        if len(id) % 2 == 1:
            return False

        mid_point = len(id) // 2
        start = id[0:mid_point]
        end = id[mid_point:]

        return start == end

    def is_id_invalid_by_n_repetition(self, id):
        s = id
        n = len(s)

        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue

            chunk = s[:k]
            repeats = n // k

            if repeats >= 2 and chunk * repeats == s:
                return True

        return False
