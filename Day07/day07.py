# Read input file and create dictionary of equations from pattern int: int int ... int
with open('input.txt') as f:
    equations = {int(line.split(':')[0]): tuple(map(int, line.split(' ')[1:])) for line in f.read().splitlines()}


# Part One: Get the sum of test values from equations that could be true
def could_be_true(equation, results):
    # Unpack equation
    test_value, numbers = equation
    # Exit condition 1
    if test_value in results:
        return test_value
    # Exit condition 2
    elif not numbers:
        return 0
    # Base case
    if len(results) == 0:
        results.add(numbers[0] + numbers[1])
        results.add(numbers[0] * numbers[1])
        return could_be_true((test_value, numbers[2:]), results)
    # Recursive case
    else:
        new_results = set()
        for num in results:
            new_results.add(num + numbers[0])
            new_results.add(num * numbers[0])
        results |= new_results
    return could_be_true((test_value, numbers[1:]), results)


total_calibration_result = 0
for eq in equations.items():
    total_calibration_result += could_be_true(eq, set())

print(f'Part One: {total_calibration_result}')
