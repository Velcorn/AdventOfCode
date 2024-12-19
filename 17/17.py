# import cupy as cp

# Read input file and parse into registers and program
with open('17_input.txt') as f:
    lines = f.readlines()
    registers = {
        'A': int(lines[0].split()[-1]),
        'B': int(lines[1].split()[-1]),
        'C': int(lines[2].split()[-1])
    }
    program = [int(x) for x in lines[-1].split()[-1].split(',')]


def get_combo_value(combo, registers):
    return combo if combo <= 3 else registers["ABC"[combo - 4]]


def run_program(registers, program):
    p = 0
    output = []
    while p < len(program) - 1:
        opcode, operand = program[p], program[p + 1]
        if opcode == 0:  # adv
            registers['A'] //= 2 ** get_combo_value(operand, registers)
        elif opcode == 1:  # bxl
            registers['B'] ^= operand
        elif opcode == 2:  # bst
            registers['B'] = get_combo_value(operand, registers) % 8
        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                p = operand
                continue
        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']
        elif opcode == 5:  # out
            output.append(get_combo_value(operand, registers) % 8)
        elif opcode == 6:  # bdv
            registers['B'] = registers['A'] // 2 ** get_combo_value(operand, registers)
        elif opcode == 7:  # cdv
            registers['C'] = registers['A'] // 2 ** get_combo_value(operand, registers)
        p += 2
    return output


def find_lowest_a(program, start, end):
    @cp.fuse
    def simulate_a_values(a_values):
        outputs = []
        for a in a_values:
            registers = {'A': a, 'B': 0, 'C': 0}
            result = run_program(registers, program)
            if result == program:
                return a  # Found match
        return -1

    a_values = cp.arange(start, end, dtype=cp.int32)
    return simulate_a_values(a_values)


# Part One: Output of the program joined by commas
output = run_program(registers, program)
print(f"Part One: {','.join(map(str, output))}")

# Part Two: Get the lowest positive inital value for register A
start = 0
end = 10 ** 9
gpu_result = find_lowest_a(program, start, end)
print(f"Part Two: {gpu_result}")
