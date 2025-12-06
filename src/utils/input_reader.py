import os
from pathlib import Path
from typing import List


def read_input(day: int, part: int = 1, use_sample: bool = False) -> List[str]:
    project_root = Path(__file__).parent.parent.parent
    
    if use_sample:
        input_file = project_root / "inputs" / f"day_{day:02d}_sample.txt"
    else:
        input_file = project_root / "inputs" / f"day_{day:02d}_input.txt"
    
    if not input_file.exists():
        if use_sample:
            raise FileNotFoundError(f"No sample file found for day {day}: {input_file}")
        else:
            raise FileNotFoundError(f"No input file found for day {day}: {input_file}")
    
    with open(input_file) as file:
        return [line for line in file]


def read_input_raw(filename: str) -> List[str]:
    project_root = Path(__file__).parent.parent.parent
    input_file = project_root / "inputs" / filename
    
    with open(input_file) as file:
        return [line for line in file]

