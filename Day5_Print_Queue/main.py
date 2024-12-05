import time
from collections import defaultdict

def get_rules(file_path: str)->list:
    with open(file_path, "r") as file:
        rules = [[int(x) for x in line.strip().split("|")] for line in file]
    return rules


def get_updates(file_path: str)->list:
    with open(file_path, "r") as file:
        updates = [[int(x) for x in line.strip().split(",")] for line in file]
    return updates


def get_grouped_rules(rules: list)-> defaultdict:       
    grouped_rules = defaultdict(set)
    for X,Y in rules:
        grouped_rules[X].add(Y)
    return grouped_rules


def check_correct_update(update: list, rules: defaultdict)->bool:
    for idx, page in enumerate(update):
        prev_pages = update[:idx]
        for prev_page in prev_pages:        
            if prev_page in rules[page]:
                return False
    return True


def order_incorrect_update(update: list, rules: defaultdict)->list:
    for idx, page in enumerate(update):
        prev_pages = update[:idx]
        for prev_idx, prev_page in enumerate(prev_pages):        
            if prev_page in rules[page]:
                update.pop(idx)
                update.insert(prev_idx, page)
                break
    return update


def part_1(updates: list, grouped_rules: defaultdict)-> int:
    return sum([update[(len(update)-1)//2] for update in updates\
                if check_correct_update(update, grouped_rules)])


def part_2(updates: list, grouped_rules: defaultdict)-> int:
    return sum(
        order_incorrect_update(update, grouped_rules)[(len(update)-1)//2] 
        for update in updates 
        if not check_correct_update(update, grouped_rules)
    )


if __name__ == '__main__':
    rules_file_path = "./Day5_Print_Queue/input_rules.txt"
    updates_file_path = "./Day5_Print_Queue/input_updates.txt"
    rules = get_rules(rules_file_path)
    updates = get_updates(updates_file_path)

    grouped_rules = get_grouped_rules(rules)

    init_t = time.perf_counter()
    part_1_solution = part_1(updates,grouped_rules)
    elapsed_time = time.perf_counter() - init_t
    print(f'Part 1 Solution: {part_1_solution}. Time taken: {elapsed_time:.6f} ms\n')
    

    init_t = time.perf_counter()
    part_2_solution = part_2(updates, grouped_rules)
    elapsed = time.perf_counter() - init_t
    print(f'Part 2 Solution: {part_2_solution}. Time taken: {elapsed_time:.6f} ms\n')
    