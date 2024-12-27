# Solution shamelessly stolen (and slightly adapted for readability) from:
# https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m40pb1x/
from functools import cache


def get_shortest_path(chars):
    # Represent empty tile as '_', '0' denotes both the number on the numpad and '^' on the dpad
    xpad = '789456123_0A<v>'
    (start_y, start_x), (end_y, end_x) = [divmod(xpad.find(c), 3) for c in chars]

    # Movement sequence, in order of priority: left, up, down, right
    sequence = (
            '<' * (start_x - end_x) +
            '0' * (start_y - end_y) +
            'v' * (end_y - start_y) +
            '>' * (end_x - start_x)
    )

    # Reverse sequence if empty tile is involved
    return sequence[::-1] if (3, 0) in [(start_y, end_x), (end_y, start_x)] else sequence


@cache
def get_sequence_length(sequence, depth):
    # Recursively calculate the length of the sequence
    if depth < 0:
        return len(sequence) + 1  # Add 1 for the activation press
    return sum(get_sequence_length(get_shortest_path(chars), depth - 1) for chars in zip('A' + sequence, sequence + 'A'))


# Read input as list of strings
with open('21_input.txt') as f:
    codes = [line.strip() for line in f]

# Part One: Sum of the complexities of the five codes with 3 intermediate robots
print(f'Part One: {sum(int(c[:3]) * get_sequence_length(c[:3], 2) for c in codes)}')

# Part Two: Sum of the complexities of the five codes with 26 intermediate robots
print(f'Part Two: {sum(int(c[:3]) * get_sequence_length(c[:3], 25) for c in codes)}')
