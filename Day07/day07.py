# Read input file and transform into dictionary of form int: int int ... int
with open('example.txt') as f:
    equations = {}
    for line in f.read().splitlines():
        key, values = line.split(':')
        equations[int(key)] = list(map(int, values.split()))


# Check if a test value can be achieved using addition, multiplication, or concatenation
def could_be_true(equation, concat=False):
    def dfs(target, numbers, current_result):
        # Base case: no more numbers to process
        if not numbers:
            return target if current_result == target else 0

        # Extract the next number
        num = numbers[0]
        remaining = numbers[1:]

        # Try all operations: addition, multiplication, and (optionally) concatenation
        if dfs(target, remaining, current_result + num):
            return target
        if dfs(target, remaining, current_result * num):
            return target
        if concat:
            concatenated = int(str(current_result) + str(num))
            if concatenated <= target and dfs(target, remaining, concatenated):
                return target

        return 0

    # Unpack equation into test value and numbers
    test_value, numbers = equation

    # Start the recursive DFS with initial result of 0
    return dfs(test_value, numbers, 0)


# Part One: Sum test values from equations where addition/multiplication work
part_one = sum(could_be_true(eq) for eq in equations.items())
print(f"Part One: {part_one}")

# Part Two: Sum test values with addition, multiplication, or concatenation
part_two = sum(could_be_true(eq, concat=True) for eq in equations.items())
print(f"Part Two: {part_two}")
