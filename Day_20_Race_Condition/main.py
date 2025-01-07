import time
import heapq
from collections import defaultdict


def get_racetrack(file_path: str) -> dict:
    with open(file_path, "r") as file:
        input = list(map(str.strip, file.readlines()))
    return {i + j*1j: col
            for i, row in enumerate(input)
            for j, col in enumerate(row)
            if col != "#"}     


def dijkstra_maze_pathfinding(maze: dict)-> tuple:

    start, = [s for s in maze if maze[s] == "S"]

    best = float('inf')
    distance = defaultdict(lambda: float('inf'))
        
    MOVES = [1, -1, 1j, -1j]

    todo = [(0, start)]
    
    while todo:
        value, position = heapq.heappop(todo)        

        if value > distance[position]: continue

        distance[position] = value
        
        if maze.get(position) == "E" and value <= best:
            best = value
        
        for step in MOVES:
            new_position = position + step
            if new_position not in maze: continue                

            new_value = value + 1
            
            if new_value < distance[new_position]:
                heapq.heappush(todo, (
                    new_value,
                    new_position,
                ))
    
    return  distance


def part1(racetrack: dict) -> int:
    distance = dijkstra_maze_pathfinding(racetrack)
    time_saved_target = 100
    CHEAT_MOVES = list(map(lambda x: x*2, [1, -1, 1j, -1j]))

    count = 0
    for pos, dist in distance.items():
        for cheat_move in CHEAT_MOVES:
            new_pos = pos + cheat_move
            if new_pos in racetrack and distance[new_pos] - dist - 2 >= time_saved_target:
                count += 1
    return count


def part2(racetrack: dict) -> int:
    distance = dijkstra_maze_pathfinding(racetrack)
    time_saved_target = 100
    cheat_max_duration = 20

    count = 0
    for pos, dist in distance.items():
        for cheat_duration in range(2,cheat_max_duration+1):
            for dx in range(cheat_duration+1):
                dy = cheat_duration - dx
                for cheat_move in set([complex(dx,dy),complex(-dx,dy),complex(dx,-dy),complex(-dx,-dy)]):
                    new_pos = pos + cheat_move
                    if new_pos not in racetrack: continue
                    if distance[new_pos] - dist - cheat_duration >= time_saved_target:
                        count += 1


if __name__ == '__main__':
    file_path = "./Day_20_Race_Condition/input.txt"
    racetrack = get_racetrack(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(racetrack)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(racetrack)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')