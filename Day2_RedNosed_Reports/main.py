import time


def get_reports(file_path: str) -> list:
    with open(file_path, "r") as file:
        reports = [([int(level) for level in line.split()]) for line in file]
    return reports


def is_safe_report(report):
    diff = report[1] - report[0]
    if abs(diff) > 3 or diff == 0:
        return False
    
    increase = diff > 0

    prev_level = report[0]
    for level in report[1:]:
        diff = level - prev_level
        if abs(diff) > 3 or (diff <= 0 and increase) or (diff >= 0 and not increase):
            return False
        prev_level = level

    return True


def part_1(reports: list) -> int:   
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports += 1

    return safe_reports


def part_2(reports: list) -> int:
    safe_reports = 0
    for report in reports:    
        if is_safe_report(report):
            safe_reports += 1
        else:
            for level_idx in range(len(report)):
                popped_level_report = report[:level_idx] + report[level_idx+1:]
                if is_safe_report(popped_level_report):
                    safe_reports += 1 
                    break

    return safe_reports

if __name__ == '__main__':
    file_path = "./Day2_RedNosed_Reports/input.txt"
    reports = get_reports(file_path)

    init_t = time.perf_counter()
    part_1_solution = part_1(reports)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} s\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(reports)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} s\n')
    
