# Read input file and create dictionary of equations from the pattern int: int int ... int
with open('input.txt') as f:
    equations = {int(line.split(':')[0]): tuple(map(int, line.split(' ')[1:])) for line in f.read().splitlines()}


# Check if a test value can be achieved using addition, multiplication, or concatenation
def could_be_true(equation, concat=False):
    # Unpack equation into test value and numbers
    test_value, numbers = equation

    # Initialize results
    results = {0}

    # Iterate over the rest of the numbers, applying addition and multiplication (and concatenation if enabled)
    for num in numbers:
        new_results = set()
        for res in results:
            new_results.add(res + num)
            new_results.add(res * num)
            if concat:
                new_results.add(int(str(res) + str(num)))
        # Update results with new results that are less than or equal to the test value
        results = {res for res in new_results if res <= test_value}

    return test_value if test_value in results else 0


# Part One: Sum test values from equations where addition/multiplication work
part_one = sum(could_be_true(eq) for eq in equations.items())
print(f"Part One: {part_one}")

# Part Two: Sum test values with addition, multiplication, or concatenation
part_two = sum(could_be_true(eq, concat=True) for eq in equations.items())
print(f"Part Two: {part_two}")
