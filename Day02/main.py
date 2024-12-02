# Iterate over lines, calculate the differences between consecutive numbers and check if they are in the correct range
# (1 to 3) and have the same sign
with open('input.txt', 'r') as file:
    safe_reports = 0
    for line in file:
        numbers = list(map(int, line.split()))
        is_safe = True
        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            if i == 0:
                sign = diff > 0
            if sign != (diff > 0) or not 1 <= abs(diff) <= 3:
                is_safe = False
                break
        if is_safe:
            safe_reports += 1
print(safe_reports)
