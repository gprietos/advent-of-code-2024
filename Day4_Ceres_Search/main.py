import re
import time
from collections import defaultdict
from typing import Callable


def get_word_search(file_path: str) -> list:
    with open(file_path, "r") as file:
        word_search = [line.strip() for line in file]
    return word_search


def find_patterns(lines: list, pattern: str) -> int:       
    return sum([len(re.findall(pattern,line)) for line in lines])


def get_group(word_search: list, func: Callable):
    grouping = defaultdict(list)
    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            grouping[func(i,j)].append(word_search[i][j])
    return [''.join(grouping[key]) for key in sorted(grouping)]


def part_1(word_search: list) -> int:
    cols = get_group(word_search, lambda i,j: j)
    rows = get_group(word_search, lambda i,j: i)
    fdiag = get_group(word_search, lambda i,j: i+j)
    bdiag = get_group(word_search, lambda i,j: i-j)

    pattern = r"XMAS"
    pattern_reverse = pattern[::-1]

    groups = [rows,cols,fdiag,bdiag]
    patterns = [pattern, pattern_reverse]

    return sum([sum([find_patterns(group,p) for group in groups]) for p in patterns])
   

def is_x_mas(word_search: list, i: int, j:int) -> bool:
    return (word_search[i][j] == 'A' and 
            set(word_search[i-1][j-1] + word_search[i+1][j+1]) == {"M", "S"} and 
            set(word_search[i+1][j-1] + word_search[i-1][j+1]) == {"M", "S"})


def part_2(word_search: list) -> int:
    return sum(
        is_x_mas(word_search, i, j)
        for i in range(1, len(word_search) - 1)
        for j in range(1, len(word_search[i]) - 1)
    )



if __name__ == '__main__':
    file_path = "./Day4_Ceres_Search/input.txt"
    word_search = get_word_search(file_path)

    init_t = time.perf_counter()
    part_1_solution = part_1(word_search)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} ms\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(word_search)
    elapsed = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} ms\n')
    
