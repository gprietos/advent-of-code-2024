import time
import copy

def get_gridmap_and_guard_pos(file_path: str):
    with open(file_path, "r") as file:
        gridmap = [[pos for pos in line.strip()]  for line in file]
    
    for row in range(len(gridmap)):
        for col in range(len(gridmap[row])):
            if gridmap[row][col] == "^":
                return gridmap, [row,col]
    return None


def guard_patrol(grid_map: list, guard_pos: list)->set:   
    guard_dirs = [(-1,0),(0,1),(1,0),(0,-1)] # "up","right","down","left"
    guard_dir = 0

    seen = set()
    seen.add((guard_pos[0],guard_pos[1]))
    while True:
        dx,dy = guard_dirs[guard_dir]
        new_row, new_col = [guard_pos[0] + dx, guard_pos[1] + dy]

        if new_row>=len(grid_map) or new_col>=len(grid_map[0]):
            break

        if grid_map[new_row][new_col] == "#":
            guard_dir = (guard_dir+1)%4
            continue
        
        guard_pos = [new_row, new_col]
        seen.add((new_row,new_col))

    return seen


def check_loop(grid_map, guard_pos, guard_dir):
    guard_dirs = [(-1,0),(0,1),(1,0),(0,-1)] # "up","right","down","left"
    seen = set()

    while True:

        guard_pos_dir = (guard_pos[0],guard_pos[1],guard_dir)
        if guard_pos_dir in seen:
            return True
        seen.add((guard_pos[0],guard_pos[1],guard_dir))

        dx,dy = guard_dirs[guard_dir]
        new_row, new_col = [guard_pos[0] + dx, guard_pos[1] + dy]

        if new_row not in range(len(grid_map)) or new_col not in range(len(grid_map[0])):
            return False

        if grid_map[new_row][new_col] == "#":
            guard_dir = (guard_dir+1)%4
            continue
        
        guard_pos = [new_row, new_col]


def part_1(grid_map: list, guard_pos: list)->int:  
    return len(guard_patrol(grid_map, guard_pos))


def part_2(grid_map: list, guard_pos: list)->int: 
    guard_dir = 0
    loop_count = 0
    start_pos =  tuple(guard_pos)

    seen = guard_patrol(grid_map, guard_pos)

    for seen_pos in seen:
        if seen_pos == start_pos:
            continue
        grid_map_copy = copy.deepcopy(grid_map)
        grid_map_copy[seen_pos[0]][seen_pos[1]] = "#"

        if check_loop(grid_map_copy, guard_pos, guard_dir):
            loop_count += 1
    
    return loop_count



if __name__ == '__main__':
    grid_map, guard_pos = get_gridmap_and_guard_pos("./Day6_Guard_Gallivant/input.txt")

    init_t = time.perf_counter()
    part_1_solution = part_1(grid_map, guard_pos)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(grid_map, guard_pos)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')