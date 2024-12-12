# Read file as list
with open('input.txt') as f:
    stones = [stone for stone in f.read().split()]


def count_stones(stones, blinks):
    # Use memoization to cache results
    memo = {}

    def blink(stone, blinks):
        # Create a unique key for memoization
        key = (stone, blinks)
        # Base case: no more blinks
        if blinks == 0:
            return 1
        # Check if we've already calculated this state
        elif key in memo:
            return memo[key]
        # If stone is 0, it is replaced with 1
        elif stone == '0':
            result = blink('1', blinks - 1)
            memo[key] = result
            return result
        # If stone has even number of digits, it is split into two stones of equal length
        # with leading zeros removed from the right stone
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid]
            right = stone[mid:].lstrip('0') or '0'
            result = blink(left, blinks - 1) + blink(right, blinks - 1)
            memo[key] = result
            return result
        # Else new stone is the product of the original stone and 2024
        else:
            result = blink(str(int(stone) * 2024), blinks - 1)
            memo[key] = result
            return result

    return sum(blink(str(stone), blinks) for stone in stones)


# Part One: Get the number of stones after 25 blinks
one_stones = count_stones(stones, 25)
print(f'Part One: {one_stones}')

# Part One: Get the number of stones after 75 blinks
two_stones = count_stones(stones, 75)
print(f'Part Two: {two_stones}')
