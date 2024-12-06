import re

# Read input file
with open('input.txt') as f:
    text = f.read()

# Extract rules and updates
rule_pattern = re.compile(r"(\d+)\|(\d+)")
rules = [tuple(map(int, rule)) for rule in rule_pattern.findall(text)]

update_pattern = re.compile(r"(?:\d+,)+\d+")
updates = [list(map(int, update.split(','))) for update in update_pattern.findall(text)]

# Create a rules dictionary
rules_dict = {}
for rule in rules:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = set()
    rules_dict[rule[0]].add(rule[1])


# Function to check whether an update is sorted
def is_sorted(update, rules_dict):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules_dict[update[j]]:
                return False
    return True


# Function to sort an update based on the rules
def sort_update(update, rules_dict):
    while not is_sorted(update, rules_dict):
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[i] in rules_dict[update[j]]:
                    update.insert(j, update.pop(i))
                    break
    return update


# Part One: Sum of middle page numbers for sorted updates
sum_sorted = 0
for update in updates:
    if is_sorted(update, rules_dict):
        sum_sorted += update[len(update) // 2]

print(f"Part One: {sum_sorted}")

# Part Two: Sum of middle page numbers for unsorted updates after sorting
sum_unsorted = 0
for update in updates:
    if not is_sorted(update, rules_dict):
        sorted_update = sort_update(update, rules_dict)
        sum_unsorted += sorted_update[len(sorted_update) // 2]

print(f"Part Two: {sum_unsorted}")
