import networkx as nx
from collections import deque
from graphviz import Digraph

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

# Simulate the circuit and track depths
queue = deque(wire_conns)
while queue:
    i1, gate, i2, o = queue.popleft()
    # If both input wires have values, calculate the output wire value
    if i1 in wire_values and i2 in wire_values:
        if gate == 'AND':
            wire_values[o] = wire_values[i1] & wire_values[i2]
        elif gate == 'OR':
            wire_values[o] = wire_values[i1] | wire_values[i2]
        elif gate == 'XOR':
            wire_values[o] = wire_values[i1] ^ wire_values[i2]
    # Otherwise, add the connection back to the queue
    else:
        queue.append((i1, gate, i2, o))

# Part One: The decimal number that the wires starting with 'z' output
z_wires = {w: v for w, v in wire_values.items() if w.startswith('z')}
z_binary = ''.join(str(z_wires[w]) for w in sorted(z_wires, reverse=True))
z_decimal = int(z_binary, 2)
print(f'Part One: {z_decimal}')

# Part Two: Identify swapped wires based on depth mismatches
# Just plot the graph for manual inspection - might programmatically solve it later
x_wires = {w: v for w, v in wire_values.items() if w.startswith('x')}
x_binary = ''.join(str(x_wires[w]) for w in sorted(x_wires, reverse=True))
x_decimal = int(x_binary, 2)
y_wires = {w: v for w, v in wire_values.items() if w.startswith('y')}
y_binary = ''.join(str(y_wires[w]) for w in sorted(y_wires, reverse=True))
y_decimal = int(y_binary, 2)
xy_decimal = x_decimal + y_decimal
xy_binary = bin(xy_decimal)[2:]
print(xy_binary)
print(z_binary)
dot = Digraph(format="png")
for node in graph.nodes:
    dot.node(node)
for edge in graph.edges(data=True):
    gate = edge[2].get('gate', '')
    dot.edge(edge[0], edge[1], label=gate)
dot.render("24_circuit", view=True)
