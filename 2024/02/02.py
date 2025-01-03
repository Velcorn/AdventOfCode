# Read input file and split into lists of integers
with open('17_input.txt') as f:
    reports = [list(map(int, line.split())) for line in f]


# Part One: Check how many reports are safe
def is_safe(report):
    if len(report) < 2:
        return True
    safe = True
    sign = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not 1 <= abs(diff) <= 3:
            safe = False
            break
        if i == 0:
            sign = diff > 0
        elif sign != (diff > 0):
            safe = False
            break
    return safe


safe_reports = sum(is_safe(report) for report in reports)
print(f"Part One: {safe_reports}")


# Part Two: Check how many reports are safe with problem dampener
def is_safe_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if i > 0 and is_safe(report[:i - 1] + report[i:]):
            return True
        if is_safe(report[:i] + report[i + 1:]):
            return True
        if i + 1 < len(report) and is_safe(report[:i + 1] + report[i + 2:]):
            return True
    return False


safe_reports_dampener = sum(is_safe_dampener(report) for report in reports)
print(f"Part Two: {safe_reports_dampener}")
