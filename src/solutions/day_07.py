import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution

class Solution07(Solution):

    def part1(self) -> int:
        grid = self.create_grid()
        start_index = grid[0].find("S")
        
        beams = set()
        beams.add(start_index)
        
        split_count = self.modify_grid_and_count_double_splits(grid, beams, 1, 0)

        return split_count

    def part2(self) -> int:
        grid = self.create_grid()
        start_col = grid[0].find("S")
    
        cache = self.initialize_cache(grid, start_col)
    
        for row_index in range(1, len(grid)):
            cache = self.process_row(cache, grid[row_index])
    
        return sum(cache)

    def create_grid(self):
        grid = []
        for line in self.input_data:
            grid.append(line.rstrip())
        return grid
        
    def modify_grid_and_count_double_splits(self, grid, prev_beams: set, cur_row, split_count):
        if len(grid) == cur_row:
            return split_count
        
        beams = set()
        split_row = list(grid[cur_row])
        for idx, element in enumerate(split_row):
            if idx in prev_beams:
                if element == "^":
                    if idx != 0:
                        beams.add(idx - 1)
                    if idx != len(split_row) - 1:
                        beams.add(idx + 1)
                    split_count += 1
                else:
                    beams.add(idx)
        
        for idx in range(len(split_row)):
            if idx in beams:
                split_row[idx] = "|"
        
        grid[cur_row] = "".join(split_row)        

        return self.modify_grid_and_count_double_splits(grid, beams, cur_row + 1, split_count)
        
    def initialize_cache(self, grid, start_col):
        cache = [0] * len(grid[0])
        cache[start_col] = 1
        return cache
        
    def process_row(self, prev_cache, row):
        next_cache = [0] * len(row)
    
        for col in range(len(row)):
            if prev_cache[col] == 0:
                continue
            
            cell = row[col]
    
            if cell == '.':
                next_cache[col] += prev_cache[col]
    
            elif cell == '^':
                if col > 0:
                    next_cache[col - 1] += prev_cache[col]
                if col < len(row) - 1:
                    next_cache[col + 1] += prev_cache[col]
    
        return next_cache