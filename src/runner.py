"""CLI runner for Advent of Code solutions."""

import argparse
import importlib
from typing import Optional

from utils.input_reader import read_input


SOLUTION_MODULES = {
    1: "solutions.day_01.Solution01",
    2: "solutions.day_02.Solution02",
    3: "solutions.day_03.Solution03",
    4: "solutions.day_04.Solution04",
    5: "solutions.day_05.Solution05",
    6: "solutions.day_06.Solution06",
    7: "solutions.day_07.Solution07",
    8: "solutions.day_08.Solution08",
    9: "solutions.day_09.Solution09",
    10: "solutions.day_10.Solution10",
    11: "solutions.day_11.Solution11",
    12: "solutions.day_12.Solution12",
}


def get_solution_class(day: int):
    """Get the solution class for a given day.
    
    Args:
        day: Day number (1-25).
    
    Returns:
        Solution class for the day.
    
    Raises:
        ValueError: If solution for the day doesn't exist.
    """
    if day not in SOLUTION_MODULES:
        raise ValueError(f"Solution for day {day} not found")
    
    module_path, class_name = SOLUTION_MODULES[day].rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def run_day(day: int, part: Optional[int] = None) -> None:
    """Run solution for a specific day.
    
    Args:
        day: Day number (1-25).
        part: Part number (1 or 2), or None to run both.
    """
    print(f"\n{'='*60}")
    print(f"Day {day}: Running solution(s)")
    print(f"{'='*60}")
    
    try:
        solution_class = get_solution_class(day)
        
        try:
            input_data = read_input(day, 1)
        except FileNotFoundError:
            input_data = read_input(day, 2)
        
        solution = solution_class(input_data)
        
        if part is None or part == 1:
            print(f"\nPart 1:")
            answer1 = solution.part1()
            print(f"   Answer: {answer1}")
        
        if part is None or part == 2:
            try:
                input_data_part2 = read_input(day, 2)
                solution2 = solution_class(input_data_part2)
                print(f"\nPart 2:")
                answer2 = solution2.part2()
                print(f"   Answer: {answer2}")
            except FileNotFoundError:
                print(f"\nPart 2:")
                answer2 = solution.part2()
                print(f"   Answer: {answer2}")
        
    except FileNotFoundError as e:
        print(f"Error: Input file not found for day {day}")
        print(f"   {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error running solution: {e}")
        import traceback
        traceback.print_exc()


def run_all() -> None:
    """Run all available solutions."""
    print("\n" + "="*60)
    print("Running all Advent of Code 2025 solutions")
    print("="*60)
    
    for day in sorted(SOLUTION_MODULES.keys()):
        run_day(day)
    
    print("\n" + "="*60)
    print("All solutions completed!")
    print("="*60 + "\n")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2025 solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all              # Run all solutions
  %(prog)s --day 1            # Run both parts of day 1
  %(prog)s --day 1 --part 1   # Run only part 1 of day 1
  %(prog)s -d 5 -p 2          # Run only part 2 of day 5
        """
    )
    
    parser.add_argument(
        "-d", "--day",
        type=int,
        choices=range(1, 13),
        metavar="N",
        help="Run solution for day N (1-12)"
    )
    
    parser.add_argument(
        "-p", "--part",
        type=int,
        choices=[1, 2],
        metavar="N",
        help="Run only part N (1 or 2)"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all available solutions"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.all and (args.day or args.part):
        parser.error("--all cannot be used with --day or --part")
    
    if args.part and not args.day:
        parser.error("--part requires --day to be specified")
    
    if not args.all and not args.day:
        parser.error("Either --all or --day must be specified")
    
    # Run solutions
    if args.all:
        run_all()
    else:
        run_day(args.day, args.part)


if __name__ == "__main__":
    main()

