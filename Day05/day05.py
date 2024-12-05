import re

# Read input file
with open('input.txt') as f:
    text = f.read()


# Part One: Get the sum of middle page numbers from sorted updates

# Extract tuples of form x|y where x, y are numbers using regex
rule_pattern = re.compile(r"(\d+)\|(\d+)")
rules = rule_pattern.findall(text)
rules = [tuple(map(int, rule)) for rule in rules]

# Create a dictionary for each number containing the set of numbers that come after it
rules_dict = {}
for rule in rules:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = {rule[1]}
        rules_dict[rule[1]] = set()
    else:
        rules_dict[rule[0]].add(rule[1])

# Sort rules_dict for convenience
rules_dict = dict(sorted(rules_dict.items()))


# Function to check whether an update is already sorted correctly
def is_sorted(update, rules_dict):
    update_ = update.copy()
    while update_:
        page = update_[0]
        update_ = update_[1:]
        if not update_:
            return True
        if any(page in rules_dict[num] for num in update_):
            return False


# Extract lists of form a, b, ..., z using regex where a, b, ..., z are integers
update_pattern = re.compile(r"(?:\d+,)+\d+")
updates = update_pattern.findall(text)
updates = [list(map(int, update.split(','))) for update in updates]
# Calculate the sum of middle page numbers from sorted updates
sum_sorted = 0
for update in updates:
    if is_sorted(update, rules_dict):
        sum_sorted += update[len(update) // 2]

print(f"Part One: {sum_sorted}")


# Part Two: Get the sum of middle page numbers from unsorted updates after sorting them

# Function to sort an update based on given rules
def sort_update(update, rules_dict):
    update_ = update.copy()
    sorted_update = []
    while update_:
        for page in update_:
            if not any(page in rules_dict[num] for num in update_):
                sorted_update.append(page)
                update_.remove(page)
    return sorted_update


# Calculate the sum of middle page numbers from unsorted updates after sort
sum_unsorted = 0
for update in updates:
    if not is_sorted(update, rules_dict):
        update = sort_update(update, rules_dict)
        sum_unsorted += update[len(update) // 2]

print(f"Part Two: {sum_unsorted}")
