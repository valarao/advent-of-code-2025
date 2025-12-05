import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution05(Solution):
    def part1(self) -> int:
        ranges = self.get_ranges()
        available_ingredients = self.get_available_ingredients()

        num_of_fresh_ingredients = 0
        for ingredient in available_ingredients:
            if self.is_ingredient_fresh(ingredient, ranges):
                num_of_fresh_ingredients += 1

        return num_of_fresh_ingredients

    def part2(self) -> int:
        ranges = self.get_ranges()
        num_of_fresh_ingredients = 0
        for range in ranges:
            num_of_fresh_ingredients += self.count_ingredients_in_range(range)
        return num_of_fresh_ingredients

    def get_ranges(self):
        ranges = []

        i = 0
        while self.input_data[i] != "":
            range = self.input_data[i].split("-")
            ranges.append([int(range[0]), int(range[1])])
            i += 1

        sorted_ranges = sorted(ranges, key=lambda r: r[0])
        return self.merge_ranges(sorted_ranges)

    def merge_ranges(self, ranges):
        merged_ranges = [ranges[0]]
        current_range = merged_ranges[0]
        for i in range(1, len(ranges)):
            candidate_range = ranges[i]
            if current_range[1] >= candidate_range[0]:
                current_range[1] = max(current_range[1], candidate_range[1])
            else:
                merged_ranges.append(candidate_range)
                current_range = candidate_range

        return merged_ranges

    def count_ingredients_in_range(self, range):
        start = range[0]
        end = range[1]
        return end - start + 1

    def get_available_ingredients(self):
        seen_range = False
        available_ingredients = []
        for x in self.input_data:
            if seen_range:
                available_ingredients.append(int(x))
            elif x == "":
                seen_range = True
        return sorted(available_ingredients)

    def is_ingredient_fresh(self, ingredient, ranges):
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                return True
        return False
