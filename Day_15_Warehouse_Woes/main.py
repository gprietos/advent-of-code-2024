import time
from itertools import takewhile

MOVES = {
    "^": -1,
    "v": 1,
    ">": 1j,
    "<": -1j,
}


def get_warehouse(warehouse_path: str) -> dict:
    with open(warehouse_path, "r") as f:
        warehouse = list(map(lambda x: x.strip(), f.readlines()))

    return {i + j*1j: col
            for i, row in enumerate(warehouse)
            for j, col in enumerate(row)
            }


def get_second_warehouse(warehouse_path: str) -> dict:
    with open(warehouse_path, "r") as f:
        warehouse = list(map(lambda x: x.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'), f.readlines()))

    return {i + j*1j: col
            for i, row in enumerate(warehouse)
            for j, col in enumerate(row)
            }    


def get_movements(movements_path: str) -> list:
    with open(movements_path, "r") as f:
        return f.read().replace("\n", "")
 

def get_moveable_items(warehouse, pos, dir):
    def moveable(pos): return warehouse[pos] in ["O", "@"]
    def get_line(pos, warehouse):
        while pos in warehouse:
            yield pos
            pos += dir

    return list(takewhile(moveable, get_line(pos, warehouse)))


def get_moveable_items_part2(warehouse, pos, dir):
    def moveable(pos): return warehouse[pos] in ["@", "[", "]"]
    def get_line(pos, warehouse):
        while pos in warehouse:
            yield pos
            pos += dir
    if dir in [1j, -1j]:
        return list(takewhile(moveable, get_line(pos, warehouse)))
    else:
        moveable_items = {pos}
        if warehouse[pos+dir] in ["[","]"]: moveable_items |= get_moveable_items_part2(warehouse, pos+dir, dir)
        if warehouse[pos+dir] == "[": moveable_items |= get_moveable_items_part2(warehouse, pos+dir+MOVES[">"], dir)
        if warehouse[pos+dir] == "]": moveable_items |= get_moveable_items_part2(warehouse, pos+dir+MOVES["<"], dir)

        return moveable_items


def print_grid(grid_dict):
    real_coords = [int(key.real) for key in grid_dict.keys()]
    imag_coords = [int(key.imag) for key in grid_dict.keys()]
    
    min_real, max_real = min(real_coords), max(real_coords)
    min_imag, max_imag = min(imag_coords), max(imag_coords)

    for i in range(min_real, max_real + 1):
        row = ""
        for j in range(min_imag, max_imag + 1):
            complex_key = complex(i, j)
            if complex_key in grid_dict:
                row += grid_dict[complex_key]
            else:
                row += " "
        print(row)


def part1(warehouse: dict, movements:str) -> int:
    for move in movements:
        robot, = [p for p in warehouse if warehouse[p] == "@"]
        moveable_items = get_moveable_items(warehouse, robot, MOVES[move])

        if warehouse[moveable_items[-1] + MOVES[move]] == "#": continue

        for item in reversed(moveable_items):
            warehouse[item+MOVES[move]] = warehouse[item]
            warehouse[item] = "."

    return sum(map(lambda x: int(100*x.real + x.imag), [p for p in warehouse if warehouse[p] == "O"]))
 

def part2(warehouse: dict, movements:str) -> int:
    for move in movements:
        robot, = [p for p in warehouse if warehouse[p] == "@"]
        moveable_items = get_moveable_items_part2(warehouse, robot, MOVES[move])

        if any(warehouse[it + MOVES[move]] == "#" for it in moveable_items) : continue      

        updates = {item+MOVES[move] : warehouse[item] for item in moveable_items}
        warehouse.update({item : "." for item in moveable_items})
        warehouse.update(updates)

        # print_grid(warehouse)

    return sum(map(lambda x: int(100*x.real + x.imag), [p for p in warehouse if warehouse[p] == "["]))


if __name__ == '__main__':
    warehouse_path = "./Day_15_Warehouse_Woes/input_warehouse.txt"
    movements_path = "./Day_15_Warehouse_Woes/input_movements.txt"
    warehouse = get_warehouse(warehouse_path)
    warehouse2 = get_second_warehouse(warehouse_path)
    movements = get_movements(movements_path)


    init_t = time.perf_counter()
    part_1_solution = part1(warehouse, movements)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part2(warehouse2, movements)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')