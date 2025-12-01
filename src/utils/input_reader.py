import os
from pathlib import Path
from typing import List


def read_input(day: int, part: int = 1) -> List[str]:
    project_root = Path(__file__).parent.parent.parent
    input_file = project_root / "inputs" / f"day_{day:02d}_part_{part}.txt"
    
    if not input_file.exists():
        raise FileNotFoundError(f"No input file found for day {day}, part {part}: {input_file}")
    
    with open(input_file) as file:
        return [line.rstrip() for line in file]


def read_input_raw(filename: str) -> List[str]:
    project_root = Path(__file__).parent.parent.parent
    input_file = project_root / "inputs" / filename
    
    with open(input_file) as file:
        return [line.rstrip() for line in file]

