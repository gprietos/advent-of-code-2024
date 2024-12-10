import time


def get_topographic_map(file_path):
    with open(file_path, "r") as file:
        topographic_map = [line.strip() for line in file]
    return topographic_map


def get_start_set(topographic_map: str) -> set:
    start_set = set()
    for i, row in enumerate(topographic_map):
        for j, col in enumerate(row):
            if col == '0':
                start_set.add((i,j))
    return start_set


def in_topographic_map_bounds(pos: tuple, topographic_map: list) -> bool:
    if ((0 <= pos[0] < len(topographic_map)) and 
        (0 <= pos[1] < len(topographic_map[0]))):
        return True    
    return False


directions = [(-1,0),(0,1),(1,0),(0,-1)] # "up","right","down","left"


def explore_trail(start_pos: tuple, topographic_map: list, trailhead_ends: set) -> None:
    ratings = 0
    start_pos_value = topographic_map[start_pos[0]][start_pos[1]]
    if start_pos_value == "9":        
        trailhead_ends.add((start_pos[0],start_pos[1]))        
        return 1

    for dir in directions:
        new_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
        if not in_topographic_map_bounds(new_pos, topographic_map):
           continue
        
        new_pos_value = topographic_map[new_pos[0]][new_pos[1]]
        if (int(new_pos_value) - int(start_pos_value)) != 1:
            continue
        
        ratings += explore_trail(new_pos,topographic_map,trailhead_ends)
    
    return ratings


def part1(topographic_map: list) -> int:

    start_set = get_start_set(topographic_map)

    total_trailheads = 0
    for start in start_set:
        trailhead_ends = set()
        explore_trail(start,topographic_map,trailhead_ends)
        total_trailheads += len(trailhead_ends)
    
    return total_trailheads   


def part2(topographic_map: list) -> int:

    start_set = get_start_set(topographic_map)

    total_rating = 0
    for start in start_set:
        trailhead_ends = set()
        total_rating += explore_trail(start,topographic_map,trailhead_ends)
    
    return total_rating



if __name__ == '__main__':
    file_path = "./Day10_Hoof_It/input.txt"
    topographic_map = get_topographic_map(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(topographic_map)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(topographic_map)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')