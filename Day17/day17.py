# Read input file and parse into registers and program
with open('input.txt') as f:
    lines = f.readlines()
    reg_a = int(lines[0].split()[-1])
    reg_b = int(lines[1].split()[-1])
    reg_c = int(lines[2].split()[-1])
    program = [int(x) for x in lines[-1].split()[-1].split(',')]

# Part One: Output of the program joined by commas
output = []

