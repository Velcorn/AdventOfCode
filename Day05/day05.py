from collections import defaultdict, deque
import re

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
def is_sorted(update, rules_dict):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules_dict[update[j]]:
                return False
    return True


# Topological sorting function
def sort_update(update, rules_dict):
    # Create graph for the update
    graph = defaultdict(set)
    indegree = {page: 0 for page in update}

    for page in update:
        for dependency in rules_dict.get(page, set()):
            if dependency in update:
                graph[page].add(dependency)
                indegree[dependency] += 1

    # Topological sort (Kahn's Algorithm)
    queue = deque([page for page in update if indegree[page] == 0])
    sorted_update = []

    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in graph[page]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


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
