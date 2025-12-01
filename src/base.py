from abc import ABC, abstractmethod
from typing import List, Any


class Solution(ABC):

    def __init__(self, input_data: List[str]):
        self.input_data = input_data

    @abstractmethod
    def part1(self) -> Any:
        pass

    @abstractmethod
    def part2(self) -> Any:
        pass

    def solve(self) -> tuple[Any, Any]:
        return self.part1(), self.part2()

