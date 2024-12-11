# Read file as list
with open('example.txt') as f:
    stones = [stone for stone in f.read().split()]


def blink(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            size = len(stone)
            if stone == '0':
                new_stones.append('1')
            elif size % 2 == 0:
                half = size // 2
                left = stone[:half]
                right = stone[half:].lstrip('0') or '0'
                new_stones.extend([left, right])
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
    return stones


# Part One: Get the number of stones after 25 blinks
one_stones = blink(stones, 25)
print(f'Part One: {len(one_stones)}')

# Part One: Get the number of stones after 75 blinks
two_stones = blink(stones, 75)
print(f'Part Two: {len(two_stones)}')
