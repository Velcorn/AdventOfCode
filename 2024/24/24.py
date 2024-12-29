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


# Simulate the circuit
wire_conns = sorted(wire_conns, reverse=True)
while wire_conns:
    for wc in wire_conns:
        i1, i2, gate, o = wc
        if i1 in wire_values and i2 in wire_values:
            if gate == 'AND':
                wire_values[o] = wire_values[i1] & wire_values[i2]
            elif gate == 'OR':
                wire_values[o] = wire_values[i1] | wire_values[i2]
            else:
                wire_values[o] = wire_values[i1] ^ wire_values[i2]
            wire_conns.remove(wc)

# Part One: The decimal number that the wires starting with z output
z_wires = {w: v for w, v in wire_values.items() if w.startswith('z')}
z_binary = ''.join(str(z_wires[w]) for w in sorted(z_wires, reverse=True))
z_decimal = int(z_binary, 2)
print(f'Part One: {z_decimal}')

# Part Two: The eight wires involved in a swap sorted alphabetically and joined with commas
