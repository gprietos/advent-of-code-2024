import time
import numpy as np
import re


def get_machines(file_path: str) -> list:
    with open(file_path, "r") as f:
        data = f.read()
        machines = data.strip().split("\n\n")

    button_a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    button_b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    machine_list = []
    for machine in machines:
        a_match = list(map(lambda x: int(x), re.findall(button_a_pattern, machine)[0]))
        b_match = list(map(lambda x: int(x), re.findall(button_b_pattern, machine)[0]))
        prize_match = list(map(lambda x: int(x), re.findall(prize_pattern, machine)[0]))
        machine_list.append({"A" : a_match,
                             "B" : b_match,
                             "Prize" : prize_match})

    return machine_list


def part1(machines: list, conv_error: int = 0) -> int:
    token_count = 0
    for machine in machines:
        A = np.array([[machine["A"][0],machine["B"][0]],[machine["A"][1],machine["B"][1]]])
        b = np.array([machine["Prize"][0] + conv_error, machine["Prize"][1] + conv_error])
        # if np.linalg.det(A) == 0: continue  # Cramer's rule ()
        a_press_count, b_press_count = np.linalg.solve(A, b)
        
        if a_press_count < 0 or b_press_count < 0 or abs(a_press_count - round(a_press_count)) > 0.001 \
           or abs(b_press_count - round(b_press_count)) > 0.001:
            continue
        token_count += 3*round(a_press_count) + round(b_press_count)

    return token_count

if __name__ == '__main__':
    file_path = "./Day_13_Claw_Contraption/input.txt"
    machines = get_machines(file_path)

    init_t = time.perf_counter()
    part_1_solution = part1(machines)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part1(machines, conv_error=10000000000000)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')