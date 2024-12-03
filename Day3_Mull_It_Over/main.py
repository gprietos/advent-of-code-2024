import re
import time


def get_corrupted_instructions(file_path: str) -> list:
    with open(file_path, "r") as file:
        corrupted_instructions = file.readlines()
    return corrupted_instructions


def mul(x: int, y: int) -> int:
    return x*y


def get_uncorrupted_instructions(corrupted_instructions: list, pattern: str) -> list:
    return [match for line in corrupted_instructions for match in re.findall(pattern, line)]


def part_1(corrupted_instructions: list) -> int:   

    pattern_mul = r"mul\(\d{1,3},\d{1,3}\)"
    uncorrupted_instructions = get_uncorrupted_instructions(corrupted_instructions, pattern_mul)
    
    mul_total = sum(eval(instruction) for instruction in uncorrupted_instructions)

    return  mul_total
   

def part_2(corrupted_instructions: list) -> int:

    pattern_mul  = r"mul\(\d{1,3},\d{1,3}\)"
    pattern_do   = r"do\(\)"
    pattern_dont = r"don't\(\)"

    pattern = f"{pattern_mul}|{pattern_do}|{pattern_dont}"
    uncorrupted_instructions = get_uncorrupted_instructions(corrupted_instructions, pattern)

    flag = True
    mul_total=0
    for instruction in uncorrupted_instructions:
        if bool(re.match(pattern_do,instruction)):
            flag = True
        elif bool(re.match(pattern_dont,instruction)):
            flag = False
        elif flag:
            mul_total += eval(instruction)

    return mul_total


if __name__ == '__main__':
    file_path = "./Day3_Mull_It_Over/input.txt"
    corrupted_instructions = get_corrupted_instructions(file_path)

    init_t = time.perf_counter()
    part_1_solution = part_1(corrupted_instructions)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} ms\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(corrupted_instructions)
    elapsed = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} ms\n')
    
