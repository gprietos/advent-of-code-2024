import time
import numpy as np
from collections import defaultdict
from itertools import combinations,count


def get_antena_map(file_path: str)-> str:
    with open(file_path, "r") as file:
        antena_map = [line.strip() for line in file]
    return antena_map


def get_frecuencies_pos(antena_map: str)-> defaultdict:
    frecuencies = defaultdict(set)
    for i in range(len(antena_map)):
        for j in range(len(antena_map[i])):
            if antena_map[i][j] != ".":
                frecuencies[antena_map[i][j]].add((i,j))
    return frecuencies


def add_antinodes_by_direction(start_antinode, step, antinode_set, antena_map):
    for i in count():
        antinode = start_antinode + i*step
        if not (0 <= antinode[0] < len(antena_map) and 0 <= antinode[1] < len(antena_map[0])):
            break
        antinode_set.add(tuple(antinode.tolist()))


def part1(antena_map: str)->int:

    frecuencies = get_frecuencies_pos(antena_map)

    antinode_set = set()
    for frec in frecuencies:
        for pair in sorted(combinations(frecuencies[frec],r=2)):
            pair = np.array(pair)     
            diff = pair[1] - pair[0]
            antinodes = [pair[0]-diff,pair[1]+diff]
            for antinode in antinodes:
                if 0 <= antinode[0] < len(antena_map) and 0 <= antinode[1] < len(antena_map[0]):
                    antinode_set.add(tuple(antinode.tolist()))
    
    return len(antinode_set)


def part2(antena_map: str)->int:

    frecuencies = get_frecuencies_pos(antena_map)

    antinode_set = set()
    for frec in frecuencies:
        for pair in sorted(combinations(frecuencies[frec],r=2)):
            pair = np.array(pair)     
            diff = pair[1] - pair[0]

            add_antinodes_by_direction(pair[0], -diff, antinode_set, antena_map)
            add_antinodes_by_direction(pair[1], diff, antinode_set, antena_map)                    
    
    return len(antinode_set)



if __name__ == '__main__':
    file_path = "./Day8_Resonant_Collinearity/input.txt"
    antena_map = get_antena_map(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(antena_map)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(antena_map)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')