# Read file as list
with open('input.txt') as f:
    stones = [stone for stone in f.read().split()]


def count_stones(stones, blinks):
    # Use memoization to cache results
    memo = {}

    def blink(stone, blinks):
        # Create a unique key for memoization
        key = (stone, blinks)

        # Check if we've already calculated this state
        if key in memo:
            return memo[key]

        # Base case: no more blinks
        if blinks == 0:
            return 1

        # If stone is 0, it becomes 1 stone
        if stone == '0':
            result = blink('1', blinks - 1)
            memo[key] = result
            return result

        # If even number of digits, splits into two stones
        if len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid]
            right = stone[mid:].lstrip('0') or '0'
            result = blink(left, blinks - 1) + blink(right, blinks - 1)
            memo[key] = result
            return result

        # Odd number of digits: multiply by 2024
        result = blink(str(int(stone) * 2024), blinks - 1)
        memo[key] = result
        return result

    # Sum the stone counts for all initial stones
    return sum(blink(str(stone), blinks) for stone in stones)


# Part One: Get the number of stones after 25 blinks
one_stones = count_stones(stones, 25)
print(f'Part One: {one_stones}')

# Part One: Get the number of stones after 75 blinks
two_stones = count_stones(stones, 75)
print(f'Part Two: {two_stones}')
