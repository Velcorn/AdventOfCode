# Read the input as list of strings
with open("02_input.txt", "r") as f:
    lines = f.read().splitlines()

wrap = 0
ribbon = 0
for line in lines:
    dims = list(map(int, line.split("x")))
    l, w, h = dims[0], dims[1], dims[2]
    wrap += 2 * l * w + 2 * w * h + 2 * h * l + min(l*w, w*h, h*l)
    dims.sort()
    smallest, second_smallest = dims[0], dims[1]
    ribbon += 2 * smallest + 2 * second_smallest + l * w * h

# Part One: Total square feet of wrapping paper
print("Part One:", wrap)

# Part Two: Total feet of ribbon
print("Part Two:", ribbon)
