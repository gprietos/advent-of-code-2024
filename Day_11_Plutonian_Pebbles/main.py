import time
from functools import cache

def get_stones(file_path: str)->list:
    with open(file_path, "r") as file:
        stones = file.readline().split(" ")
    return stones


@cache
def blink(stone: str, blink_count: int, target_blink:int) -> int:
    if blink_count == target_blink:
        return 1

    stone_count = 0
    
    if stone == "0":
        stone_count += blink("1", blink_count+1, target_blink)
    elif len(stone) % 2 == 0:
        left_stone = str(int(stone[:len(stone)//2]))
        right_stone = str(int(stone[len(stone)//2:]))
        stone_count += blink(left_stone, blink_count+1, target_blink)
        stone_count += blink(right_stone, blink_count+1, target_blink)
    else:
        stone_count += blink(str(int(stone)*2024),blink_count+1, target_blink) 

    return stone_count


def part1(stones: list, target_blink: int) -> int:
    return sum([blink(stone,0,target_blink) for stone in stones])

if __name__ == '__main__':
    file_path = "./Day_11_Plutonian_Pebbles/input.txt"
    stones = get_stones(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(stones, 25)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part1(stones, 75)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')