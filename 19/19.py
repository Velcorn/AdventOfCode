with open('19_input.txt') as f:
    lines = f.read().splitlines()
    patterns = lines[0].split(', ')
    designs = [line for line in lines[2:]]


def is_possible(design, op):
    if design in memo:
        return memo[design]
    if not design:
        return True
    result = op(
        is_possible(design[len(pattern):], op)
        for pattern in patterns
        if design.startswith(pattern)
    )
    memo[design] = result
    return result


# Part One: Number of possible designs
memo = {}
part_one = sum(is_possible(design, any) for design in designs)
print(f'{part_one}')

# Part Two: Number of different ways to make the designs
memo.clear()
part_two = sum(is_possible(design, sum) for design in designs)
print(f'{part_two}')
