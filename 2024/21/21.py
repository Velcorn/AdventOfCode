def find(pad, char):
    for y, row in enumerate(pad):
        for x, c in enumerate(row):
            if c == char:
                return x, y


def bfs(pad, start, end):
    queue = [(start, '')]
    visited = set()
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path + 'A'
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1), ]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(pad[0]) and 0 <= new_y < len(pad) and pad[new_y][new_x] != ' ':
                queue.append(((new_x, new_y), path + '^>v<'[[(0, -1), (1, 0), (0, 1), (-1, 0)].index((dx, dy))]))
    return None


# Read input as list of strings
with open('21_example.txt') as f:
    codes = [line.strip() for line in f]

# Numpad and dpad
numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
dpad = [[' ', '^', 'A'], ['<', 'v', '>']]

# Part One: The sum of the complexities of the five codes on the list
complexities = 0
for code in codes:
    r2_start = find(numpad, 'A')
    r2_buttons = ''
    for c in code:
        r2_end = find(numpad, c)
        path = bfs(numpad, r2_start, r2_end)
        r2_buttons += path
        r2_start = r2_end
    r3_start = find(dpad, 'A')
    r3_buttons = ''
    for r2b in r2_buttons:
        r3_end = find(dpad, r2b)
        path = bfs(dpad, r3_start, r3_end)
        r3_buttons += path
        r3_start = r3_end
    me_start = find(dpad, 'A')
    me_buttons = ''
    for r3b in r3_buttons:
        me_end = find(dpad, r3b)
        path = bfs(dpad, me_start, me_end)
        me_buttons += path
        me_start = me_end
    complexities += int(code.lstrip('0').rstrip('A')) * len(me_buttons)
print(f'Part One: {complexities}')
