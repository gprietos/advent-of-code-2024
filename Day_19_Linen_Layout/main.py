import time
from typing import List, Tuple
from functools import cache

def get_patterns(pattern_path: str) -> Tuple:
    with open(pattern_path, "r") as f:        
        return tuple(f.readline().split(", "))
    

def get_designs(designs_path: str) -> List:
    with open(designs_path, "r") as f:
        return [line.strip() for line in f.readlines()]
    
    
@cache
def check_design(design: List, patterns: List) -> bool:
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if check_design(design[len(pattern):], patterns):
                return True
    return False


@cache
def count_combinations_in_design(design: List, patterns: List) -> bool:
    if design == "":
        return 1
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += count_combinations_in_design(design[len(pattern):], patterns)            
    return count


def part1(patterns: List, designs: List): 
    return sum([check_design(design, patterns) for design in designs])


def part2(patterns: List, designs: List):     
    return sum([count_combinations_in_design(design, patterns) for design in designs])


if __name__ == '__main__':
    patterns_path = "/home/gprietos/AoC2024/advent-of-code-2024/Day_19_Linen_Layout/input_patterns.txt"
    designs_path = "/home/gprietos/AoC2024/advent-of-code-2024/Day_19_Linen_Layout/input_designs.txt"
    patterns = get_patterns(patterns_path)
    designs = get_designs(designs_path)

    init_t = time.perf_counter()
    part_1_solution = part1(patterns, designs)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(patterns, designs)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')