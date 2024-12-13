import time
from typing import Tuple


Point = Tuple[int, ...]
Vector = Tuple[int, ...]

directions = [(-1,0),(0,1),(1,0),(0,-1)] # "up","right","down","left"


def get_garden(file_path: str)->list:
    with open(file_path, "r") as file:
        garden = [ line.strip() for line in file.readlines()]
    return garden


def in_garden_bounds(pos: tuple, garden: list) -> bool:
    if ((0 <= pos[0] < len(garden)) and 
        (0 <= pos[1] < len(garden[0]))):
        return True    
    return False


def add2(p: Point, q: Point) -> Point: 
    return (p[0] + q[0], p[1] + q[1])


def region_fill(garden: list, plot: Point, region_set: set):
    plant_type = garden[plot[0]][plot[1]]
    area = 1
    perimeter = 0

    for dir in directions:
        neighbour_plot = add2(plot, dir)
        if neighbour_plot in region_set:
            continue
        if not in_garden_bounds(neighbour_plot, garden) \
           or garden[neighbour_plot[0]][neighbour_plot[1]] != plant_type:
            perimeter += 1
            continue
        
        region_set.add(neighbour_plot)
        region_area, region_perimeter = region_fill(garden, neighbour_plot, region_set)

        area += region_area
        perimeter += region_perimeter
    
    return area, perimeter


def get_region_sides(region: set)->int:
    def has_edge(plot: Point, dir: Vector): return plot in region and add2(plot, dir) not in region
    return sum(has_edge(plot, dir) and \
               not has_edge(add2(plot, directions[(dir_idx+1)%len(directions)]), dir)
                for plot in region
                for dir_idx, dir in enumerate(directions)
            )

def part1(garden: list) -> int:
    seen_plots_set = set()
    total_fence_cost = 0
    for row_idx in range(len(garden)):
        for col_idx in range(len(garden[row_idx])):
            if (row_idx,col_idx) in seen_plots_set:
                continue
            region_set = {(row_idx,col_idx)}
            area, perimeter = region_fill(garden, (row_idx, col_idx), region_set)
            seen_plots_set.update(region_set)
            total_fence_cost += area*perimeter

    return total_fence_cost


def part2(garden: list) -> int:
    seen_plots_set = set()
    total_fence_cost = 0
    for row_idx in range(len(garden)):
        for col_idx in range(len(garden[row_idx])):
            if (row_idx,col_idx) in seen_plots_set:
                continue
            region_set = {(row_idx,col_idx)}
            area, _ = region_fill(garden, (row_idx, col_idx), region_set)
            seen_plots_set.update(region_set)
            sides = get_region_sides(region_set)
            total_fence_cost += area*sides

    return total_fence_cost
            

if __name__ == '__main__':
    file_path = "./Day_12_Garden_Groups/input.txt"
    garden = get_garden(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(garden)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(garden)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')