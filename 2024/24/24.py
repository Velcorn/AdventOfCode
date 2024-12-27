# Read input as dict and list of lists
with open('24_p2example.txt') as f:
    lines = f.read().splitlines()
    wire_values = {}
    wire_conns = []
    for line in lines:
        if ':' in line:
            wire, value = line.split(': ')
            wire_values[wire] = int(value)
        elif '->' in line:
            i1, gate, i2, o = line.replace('-> ', '').split()
            wire_conns.append([i1, gate, i2, o])


# Part One: The decimal number that the wires starting with z output
z_wires = []
while wire_conns:
    for wc in wire_conns:
        i1, gate, i2, o = wc
        if all(i in wire_values for i in [i1, i2]):
            if gate == 'AND':
                wire_values[o] = wire_values[i1] & wire_values[i2]
            elif gate == 'OR':
                wire_values[o] = wire_values[i1] | wire_values[i2]
            else:
                wire_values[o] = wire_values[i1] ^ wire_values[i2]
            if 'z' in o:
                z_wires.append(o)
            wire_conns.remove(wc)
z_wires = sorted(z_wires, reverse=True)
binary = ''.join(str(wire_values[w]) for w in z_wires)
print(int(binary, 2))
