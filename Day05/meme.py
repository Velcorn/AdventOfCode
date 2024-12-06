import multiprocessing
import random
import re
from collections import defaultdict


# Read input file
with open('input.txt') as f:
    text = f.read()

# Extract rules and updates
rule_pattern = re.compile(r"(\d+)\|(\d+)")
rules = rule_pattern.findall(text)
rules = [tuple(map(int, rule)) for rule in rules]

update_pattern = re.compile(r"(?:\d+,)+\d+")
updates = update_pattern.findall(text)
updates = [list(map(int, update.split(','))) for update in updates]

# Create a rules dictionary
rules_dict = defaultdict(set)
for rule in rules:
    rules_dict[rule[0]].add(rule[1])


# Function to check whether an update is sorted
def is_sorted(single_update, rules_dict):
    for i in range(len(single_update)):
        for j in range(i + 1, len(single_update)):
            if single_update[i] in rules_dict[single_update[j]]:
                return False
    return True


# Function to sort an update based on the rules
def sort_update(single_update, rules_dict):
    while not is_sorted(single_update, rules_dict):
        # Iterate through the update: if the current page is in the rules of a following page, move it before that page
        for i in range(len(single_update)):
            for j in range(i + 1, len(single_update)):
                if single_update[i] in rules_dict[single_update[j]]:
                    single_update.insert(j, single_update.pop(i))
                    break
    return single_update


def bogosort_update(single_update):
    """
    Randomly shuffles the update until it's sorted according to the rules.
    """
    random.shuffle(single_update)
    return single_update


def process_update(single_update, rules_dict):
    """
    Process a single update by applying Bogosort until sorted.
    """
    while not is_sorted(single_update, rules_dict):
        single_update = bogosort_update(single_update)
    return single_update[len(single_update) // 2]  # Return the middle element


def parallel_bogosort(updates_list, rules_dict):
    """
    Use multiprocessing to apply Bogosort on each update in parallel.
    """
    with multiprocessing.Pool() as pool:
        results = pool.starmap(process_update, [(u, rules_dict) for u in updates_list])
    return sum(results)  # Sum the results of middle elements


if __name__ == '__main__':
    # Part One: Sum of middle page numbers for sorted updates
    sum_sorted = 0
    for single_update in updates:
        if is_sorted(single_update, rules_dict):
            sum_sorted += single_update[len(single_update) // 2]

    print(f"Part One: {sum_sorted}")

    # Part Two: Sum of middle page numbers for unsorted updates after sorting
    unsorted_updates = [u for u in updates if not is_sorted(u, rules_dict)]
    sum_unsorted = parallel_bogosort(unsorted_updates, rules_dict)

    print(f"Part Two: {sum_unsorted}")
