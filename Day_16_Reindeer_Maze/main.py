import time
import heapq
from collections import defaultdict
from itertools import count


def get_maze(file_path: str) -> dict:

    with open(file_path, "r") as file:
        input = [line.strip() for line in file.readlines()]
    return {i + j*1j: col
            for i, row in enumerate(input)
            for j, col in enumerate(row)
            if col != "#"}     


def dijkstra_maze_pathfinding(maze: dict)-> tuple:

    start, = [s for s in maze if maze[s] == "S"]

    seen = set()
    best = float('inf')
    distance = defaultdict(lambda: float('inf'))
    
    unique_counter = count() # unique tie-breaking
    
    MOVES_COST = [
        (1, 1),      
        (1j, 1001),  
        (-1j, 1001)  
    ]
    
    todo = [(0, next(unique_counter), start, 1j, [start])]
    
    while todo:
        value, _, position, direction, path = heapq.heappop(todo)        

        if value > distance[position, direction]:
            continue
        distance[position, direction] = value
        
        if maze.get(position) == "E" and value <= best:
            best = value
            seen.update(set(path))
        
        for step, move_cost in MOVES_COST:
            new_direction = direction * step
            new_position = position + new_direction
            if new_position not in maze:
                continue
            
            new_value = value + move_cost
            
            if new_value < distance[new_position, new_direction]:
                heapq.heappush(todo, (
                    new_value, 
                    next(unique_counter), 
                    new_position, 
                    new_direction, 
                    path + [new_position]
                ))
    
    return best, seen


def part1(maze: dict) -> int:
    best, _ = dijkstra_maze_pathfinding(maze)
    return best

def part2(maze: dict) -> int:
    _, seen = dijkstra_maze_pathfinding(maze)
    return len(seen)


if __name__ == '__main__':
    file_path = "./Day_16_Reindeer_Maze/input.txt"
    maze = get_maze(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(maze)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(maze)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')