import networkx as nx
from collections import deque
from graphviz import Digraph
from itertools import combinations


def simulate_circuit(wvs, wcs, bits=None):
    queue = deque(wcs)
    z_wires = {}
    while queue:
        i1, gate, i2, o = queue.popleft()
        # If both input wires have values, calculate the output wire value
        if i1 in wvs and i2 in wvs:
            if gate == 'AND':
                wvs[o] = wvs[i1] & wvs[i2]
            elif gate == 'OR':
                wvs[o] = wvs[i1] | wvs[i2]
            elif gate == 'XOR':
                wvs[o] = wvs[i1] ^ wvs[i2]
            if o.startswith('z'):
                z_wires[o] = wvs[o]
        # Otherwise, add the connection back to the queue
        else:
            queue.append((i1, gate, i2, o))
        if bits and len(z_wires) == bits:
            break
    z_binary = ''.join(str(z_wires[w]) for w in sorted(z_wires, reverse=True))
    return z_binary, wvs, wcs


# Read input as dict for initial wire values and list for wire connections
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
            wire_conns.append((i1, gate, i2, o))

# Create a directed graph of the circuit
graph = nx.DiGraph()
for i1, gate, i2, o in wire_conns:
    graph.add_edge(i1, o, gate=gate)
    graph.add_edge(i2, o, gate=gate)

# Part One: The decimal number that the wires starting with 'z' output
z_binary = simulate_circuit(wire_values.copy(), wire_conns)[0]
z_decimal = int(z_binary, 2)
print(f'Part One: {z_decimal}')

# Part Two: The names of all eight swapped wires sorted alphabetically and joined with commas

# Calculate expected output from x + y
x_wires = {w: v for w, v in wire_values.items() if w.startswith('x')}
x_binary = ''.join(str(x_wires[w]) for w in sorted(x_wires, reverse=True))
x_decimal = int(x_binary, 2)
y_wires = {w: v for w, v in wire_values.items() if w.startswith('y')}
y_binary = ''.join(str(y_wires[w]) for w in sorted(y_wires, reverse=True))
y_decimal = int(y_binary, 2)
xy_decimal = x_decimal + y_decimal
xy_binary = bin(xy_decimal)[2:]

# Find collision points between x+y and z, filtering following errors (~next two bits) that result from the carry bit
# (might only work for this specific circuit)
diffs = [i for i, (z, xy) in enumerate(zip(reversed(xy_binary), reversed(z_binary))) if z != xy]
filtered_diffs = []
for i, d in enumerate(diffs):
    if i == 0 or d - diffs[i - 1] > 2:
        filtered_diffs.append(d)
print(f'Part Two: {", ".join(map(str, filtered_diffs))}')

# Visualize the circuit
dot = Digraph(format="png")
for node in graph.nodes:
    dot.node(node)
for edge in graph.edges(data=True):
    gate = edge[2].get('gate', '')
    color = 'red' if gate == 'OR' else 'green' if gate == 'AND' else 'blue'
    dot.edge(edge[0], edge[1], color=color)
dot.render("24_circuit", view=True)
