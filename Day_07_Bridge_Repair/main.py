import re
import time
from itertools import product


def get_operations(file_path: str) -> list:
    pattern  = r"\d{1,3}"
    with open(file_path, "r") as file:
        return [
                [split_line[0], re.findall(pattern,split_line[1])]
                for line in file
                for split_line in [line.strip().split(":")]
        ]


def part_1(operations: list)->int:
    ops = ["+","*"]

    total_calibration_result = 0
    for operation in operations:
        result, terms = operation
        op_combs = list(product(ops, repeat=len(terms)-1))

        for op_comb in op_combs:
            res = terms[0]
            for term, op in zip(terms[1:], op_comb):
                res = eval(f"{res}{op}{term}")
            
            if res == int(result):
                total_calibration_result += int(result)
                break

    return total_calibration_result


def part_2(operations: list)->int:
    ops = ["+","*","||"]

    total_calibration_result = 0
    for operation in operations:
        result, terms = operation
        op_combs = list(product(ops, repeat=len(terms)-1))

        for op_comb in op_combs:
            res = terms[0]
            for term, op in zip(terms[1:], op_comb):
                if op == "+":
                    res = str(int(res) + int(term))
                if op == "*":
                    res = str(int(res) * int(term))
                if op == "||":
                    res = res + term
            
            if int(res) == int(result):
                total_calibration_result += int(result)
                break

    return total_calibration_result


if __name__ == '__main__':
    file_path = "./Day7_Bridge_Repair/input.txt"
    operations = get_operations(file_path)

    init_t = time.perf_counter()
    part_1_solution = part_1(operations)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(operations)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')