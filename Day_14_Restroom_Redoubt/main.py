import time
import re 
from collections import defaultdict
import math
import numpy as np
import copy


def get_robots(file_path: str) -> list:
    with open(file_path, "r") as f:
        robots = f.readlines()
    robot_pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

    robot_list = []
    for robot in robots:
        robot_info = re.match(robot_pattern, robot).groups()
        robot_list.append(list(map(int, robot_info)))

    return robot_list


def get_quadrant_robots(robots: list, wide_tiles: int, tall_tiles: int) -> defaultdict:
    quadrant_robots = defaultdict(int)
    for x, y, _, _ in robots:
        if x == wide_tiles // 2 or y == tall_tiles // 2:
            continue
        quadrant = (x > wide_tiles // 2) + 2 * (y > tall_tiles // 2)
        quadrant_robots[quadrant] += 1

    return quadrant_robots


def part1(robots: list) -> int :

    wide_tiles = 101
    tall_tiles = 103

    elapsed_time = 100

    for _ in range(elapsed_time):
        for robot in robots:
            robot_pos = np.array(robot[:2])
            robot_vel = np.array(robot[2:])

            robot_pos = (robot_pos + robot_vel) % [wide_tiles, tall_tiles]

            robot[:2] = robot_pos 

    return math.prod(get_quadrant_robots(robots, wide_tiles, tall_tiles).values())


def part2(robots: list) -> int:
    """
    An assumption has been made in which the final result occurs when every robot is at an unique position 
    (no overlap between robots). 
    Other solutions use other techniques such as https://www.youtube.com/watch?v=hhRC8XrXY1o
    """

    wide_tiles = 101
    tall_tiles = 103

    sec = 0
    while True:
        sec += 1
        
        robot_unique_pos = set()

        for robot in robots:
            robot_pos = np.array(robot[:2])
            robot_vel = np.array(robot[2:])

            robot_pos = (robot_pos + robot_vel) % [wide_tiles, tall_tiles]

            robot[:2] = robot_pos

            robot_unique_pos.add(tuple(robot_pos.tolist()))

        
        if len(robot_unique_pos) == len(robots):
            # # Uncomment this to print the Easter Egg :)
            # map = [[' ' for _ in range(wide_tiles)] for _ in range(tall_tiles)]
            # for x, y in robot_unique_pos:
            #     map[y][x] = '#'
            # print('\n'.join([''.join(row) for row in map]))
            break
    
    return sec


if __name__ == '__main__':
    file_path = "./Day_14_Restroom_Redoubt/input.txt"
    robots = get_robots(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(copy.deepcopy(robots))
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(robots)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')