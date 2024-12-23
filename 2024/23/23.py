def bron_kerbosch_pivot(r, p, x):
    if not p and not x:
        return r
    max_clique = set()
    u = max(p | x, key=lambda node: len(network[node]), default=None)
    for v in p - set(network[u]):
        clique = bron_kerbosch_pivot(r | {v}, p & set(network[v]), x & set(network[v]))
        if len(clique) > len(max_clique):
            max_clique = clique
        p.remove(v)
        x.add(v)
    return max_clique


# Read input as set of tuples
with open('23_input.txt') as f:
    connections = set(tuple(line.strip().split('-')) for line in f)

# Create a network of computers
network = {}
for a, b in connections:
    network.setdefault(a, []).append(b)
    network.setdefault(b, []).append(a)

# Part One: Number of sets of three computers that contain at least one computer that starts with t
sets_of_three = set()
for a, b in connections:
    for c in network[a]:
        if c in network[b]:
            sets_of_three.add(tuple(sorted([a, b, c])))
sets_of_t = sum(1 for a, b, c in sets_of_three if any(computer.startswith('t') for computer in [a, b, c]))
print(f'Part One: {sets_of_t}')

# Part Two: Password to get into the LAN party (the name of every computer sorted alphabetically, separated by commas)
max_clique = bron_kerbosch_pivot(set(), set(network.keys()), set())
password = ','.join(sorted(max_clique))
print(f'Part Two: {password}')
