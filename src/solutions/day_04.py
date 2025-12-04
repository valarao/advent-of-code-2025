import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution04(Solution):
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    MAX_ROLLS = 4

    def part1(self) -> int:
        r = len(self.input_data)
        c = len(self.input_data[0])

        roll_count = 0
        for i in range(r):
            for j in range(c):
                if self.is_liftable(self.input_data, i, j):
                    roll_count += 1

        return roll_count

    def part2(self) -> int:
        self.input_data = [list(row) for row in self.input_data]

        total_roll_count = 0
        while True:
            roll_count = self.mark_and_count()
            total_roll_count += roll_count
            if roll_count == 0:
                break

        return total_roll_count

    def mark_and_count(self):
        r = len(self.input_data)
        c = len(self.input_data[0])

        roll_count = 0
        marked_spots = []
        for i in range(r):
            for j in range(c):
                if self.is_liftable(self.input_data, i, j):
                    roll_count += 1
                    marked_spots.append((i, j))

        for marked_spot in marked_spots:
            self.input_data[marked_spot[0]][marked_spot[1]] = "."

        return roll_count

    def is_liftable(self, grid, i, j):
        paper_count = 0
        for dir in self.DIRS:
            candidate_dir = (i + dir[0], j + dir[1])
            if (
                0 <= candidate_dir[0]
                and 0 <= candidate_dir[1]
                and candidate_dir[0] < len(grid)
                and candidate_dir[1] < len(grid[0])
                and grid[candidate_dir[0]][candidate_dir[1]] == "@"
            ):
                paper_count += 1
        return paper_count < 4 and grid[i][j] == "@"
