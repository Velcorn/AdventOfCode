# Read input file and parse into registers and program
with open('17_input.txt') as f:
    lines = f.readlines()
    registers = {
        'A': int(lines[0].split()[-1]),
        'B': int(lines[1].split()[-1]),
        'C': int(lines[2].split()[-1])
    }
    program = [int(x) for x in lines[-1].split()[-1].split(',')]


def run_program(registers, program):
    p = 0
    output = []
    while p < len(program) - 1:
        opcode, operand = program[p], program[p + 1]
        combo = operand if operand <= 3 else registers["ABC"[operand - 4]]
        if opcode == 0:  # adv
            registers['A'] //= 2 ** combo
        elif opcode == 1:  # bxl
            registers['B'] ^= operand
        elif opcode == 2:  # bst
            registers['B'] = combo % 8
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                p = operand
                continue
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out
            output.append(combo % 8)
        elif opcode == 6:  # bdv
            registers['B'] = registers['A'] // 2 ** combo
        elif opcode == 7:  # cdv
            registers['C'] = registers['A'] // 2 ** combo
        p += 2
        print(registers)
    return output


# Part One: Output of the program joined by commas
output = run_program(registers, program)
print(registers)
print(f"Part One: {','.join(map(str, output))}")

# Part Two: Get the lowest positive inital value for register A
