def find(pad, char):
    for row, line in enumerate(pad):
        for col, c in enumerate(line):
            if c == char:
                return row, col
    return None


def bfs(pad, start, end):
    queue = [(start, '', None)]  # ((row, col), path, last_direction)
    visited = set()
    while queue:
        (row, col), path, last_dir = queue.pop(0)
        if (row, col) == end:
            return path + 'A'
        if (row, col) in visited:
            continue
        visited.add((row, col))

        # Sort directions to prioritize:
        # 1. Current direction (if it exists)
        # 2. Opposite of current direction
        # 3. Other directions
        sorted_directions = []
        if last_dir is not None:
            last_drow, last_dcol = last_dir
            for drow, dcol, arrow in directions:
                if (drow, dcol) == (last_drow, last_dcol):
                    priority = 0
                elif (drow, dcol) == (-last_drow, -last_dcol):
                    priority = 1
                else:
                    priority = 2
                sorted_directions.append((priority, (drow, dcol, arrow)))
            sorted_directions.sort()
            sorted_directions = [x[1] for x in sorted_directions]
        else:
            sorted_directions = directions

        # Try each direction in priority order
        for drow, dcol, arrow in sorted_directions:
            new_row = row + drow
            new_col = col + dcol
            if 0 <= new_row < len(pad) and 0 <= new_col < len(pad[0]) and pad[new_row][new_col] != ' ':
                queue.append(((new_row, new_col), path + arrow, (drow, dcol)))
    return None


def get_shortest_sequence(code):
    r2_start = (3, 2)
    r2_sequence = ''
    for c in code:
        r2_end = find(numpad, c)
        seq = bfs(numpad, r2_start, r2_end)
        r2_sequence += seq
        r2_start = r2_end
    r3_start = (0, 2)
    r3_sequence = ''
    for r2b in r2_sequence:
        r3_end = find(dpad, r2b)
        seq = bfs(dpad, r3_start, r3_end)
        r3_sequence += seq
        r3_start = r3_end
    my_start = (0, 2)
    my_sequence = ''
    for r3b in r3_sequence:
        my_end = find(dpad, r3b)
        seq = bfs(dpad, my_start, my_end)
        my_sequence += seq
        my_start = my_end
    return len(my_sequence)


# Read input as list of strings
with open('21_example.txt') as f:
    codes = [line.strip() for line in f if line.strip()]

# Numpad, dpad and directions
numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]
dpad = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]
directions = [
    (-1, 0, '^'),  # up
    (0, 1, '>'),  # right
    (1, 0, 'v'),  # down
    (0, -1, '<')  # left
]

# Part One: The sum of the complexities of the five codes on the list
complexities = 0
for code in codes:
    shortest_sequence = get_shortest_sequence(code)
    numeric_part = int(code.lstrip('0').rstrip('A'))
    complexities += shortest_sequence * numeric_part
print(f'Part One: {complexities}')
