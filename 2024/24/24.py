# Read input as dict and list of lists
with open('24_input.txt') as f:
    lines = f.read().splitlines()
    wire_values = {}
    wire_conns = []
    for line in lines:
        if ':' in line:
            wire, value = line.split(': ')
            wire_values[wire] = int(value)
        elif '->' in line:
            i1, gate, i2, o = line.replace('-> ', '').split()
            wire_conns.append([i1, i2, gate, o])


def get_decimal_from_prefix(wires, prefix):
    filtered = {w: v for w, v in wires.items() if w.startswith(prefix)}
    binary = ''.join(str(filtered[w]) for w in sorted(filtered, reverse=True))
    return binary, int(binary, 2)


# Simulate the circuit, tracking the connections of all y wires from input to output
yres = [[w] for w in wire_values if w.startswith('y')]
while wire_conns:
    for wc in wire_conns:
        i1, i2, gate, o = wc
        if all(i in wire_values for i in [i1, i2]):
            if gate == 'AND':
                wire_values[o] = wire_values[i1] & wire_values[i2]
            elif gate == 'OR':
                wire_values[o] = wire_values[i1] | wire_values[i2]
            else:
                wire_values[o] = wire_values[i1] ^ wire_values[i2]
            for w in yres:
                if i1 in w[-1]:
                    w[-1] = f'{i1}:{wire_values[i1]}'
                    w.append(f'{i2}:{wire_values[i2]}')
                    w.append(gate)
                    w.append(f'{o}:{wire_values[o]}')
                elif i2 == w[-1]:
                    w[-1] = f'{i2}:{wire_values[i2]}'
                    w.append(f'{i1}:{wire_values[i1]}')
                    w.append(gate)
                    w.append(f'{o}:{wire_values[o]}')
            wire_conns.remove(wc)

# Part One: The decimal number that the wires starting with z output
z_binary, z_decimal = get_decimal_from_prefix(wire_values, 'z')
print(f'Part One: {z_decimal}')


# Part Two: The eight wires involved in a swap sorted alphabetically and joined with commas

