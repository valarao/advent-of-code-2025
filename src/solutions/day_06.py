import sys
from pathlib import Path
import pprint

sys.path.insert(0, str(Path(__file__).parent.parent))

from base import Solution


class Solution06(Solution):
    def part1(self) -> int:
        problems = self.parse_worksheet_1()

        grand_total = 0
        for problem in problems:
            if problem.operator == "*":
                result = 1
                for operand in problem.operands:
                    result *= operand
                grand_total += result
            elif problem.operator == "+":
                result = 0
                for operand in problem.operands:
                    result += operand
                grand_total += result

        return grand_total

    def part2(self) -> int:
        problems = self.parse_worksheet_2()

        grand_total = 0
        for problem in problems:
            if problem.operator == "*":
                result = 1
                for operand in problem.operands:
                    result *= int(operand)
                grand_total += int(result)
            elif problem.operator == "+":
                result = 0
                for operand in problem.operands:
                    result += int(operand)
                grand_total += int(result)

        return grand_total

    def parse_worksheet_1(self):
        lines = self.parse_lines()

        current_operands = []
        problems = []
        for c in range(len(lines[0])):
            for r in range(len(lines)):
                next = lines[r][c]
                if next == "*" or next == "+":
                    problems.append(Problem(next, current_operands))
                    current_operands = []
                else:
                    current_operands.append(int(next))
        return problems

    def parse_worksheet_2(self):
        adjusted_lines = self.find_adjusted_lines()
    
        matrix = []
        for line in adjusted_lines:                
            matrix.append(list(line))

        breakpoints = self.find_breakpoints(matrix)
        ranges = self.find_ranges(breakpoints, matrix)
        
        problems = []
        for range in ranges:
                problems.append(self.construct_problem_for_range(range, matrix))

        return problems

    def parse_lines(self):
        lines = []
        for i in range(len(self.input_data) - 1):
            line = self.input_data[i]
            elements = list(filter(lambda e: e != "", line.split(" ")))
            lines.append(elements)
        lines.append(list(filter(lambda e: e != "", self.input_data[-1].split(" "))))
        return lines

    def find_adjusted_lines(self):
        adjusted_lines = []
        for r in range(len(self.input_data)):
            adjusted_lines.append(self.input_data[r][:self.input_data[r].index("\n")])
        return adjusted_lines
        
    def find_breakpoints(self, matrix):
        breakpoints = []
        for c in range(len(matrix[0])):
            is_breakpoint = True
            for r in range(len(matrix) - 1):
                if matrix[r][c] != " ":
                    is_breakpoint = False
            if is_breakpoint:
                breakpoints.append(c)

        return breakpoints
        
    def find_ranges(self, breakpoints, matrix):
        ranges = []
        start = 0
        for breakpoint in breakpoints:
            ranges.append([start, breakpoint - 1])
            start = breakpoint + 1
            
        ranges.append([start, len(matrix[0]) - 1])
        return ranges
            
    def construct_problem_for_range(self, x, matrix):
        operator = ""
        operands = []
        for c in range(x[0], x[1] + 1):
            digit = []
            for r in range(len(matrix)):
                element = matrix[r][c]
                if element == "*" or element == "+":
                    operator = element
                elif element != " ":
                    digit.append(element)
            operands.append(int("".join(digit)))

        return Problem(operator, operands)

class Problem:
    def __init__(self, operator: str, operands: list[int]):
        self.operator = operator
        self.operands = operands
