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
with open('23_example.txt') as f:
    connections = set(tuple(line.strip().split('-')) for line in f)

# Create a network of computers using sets
network = {}
for a, b in connections:
    network.setdefault(a, set()).add(b)
    network.setdefault(b, set()).add(a)

# Part One: Number of 3-cliques containing at least one 't' computer
three_cliques = {tuple(sorted([a, b, c])) for a, b in connections for c in (network[a] & network[b])}
t_cliques = sum(any(comp.startswith('t') for comp in clique) for clique in three_cliques)
print(f'Part One: {t_cliques}')

# Part Two: Password is all computers in max clique, sorted alphabetically and comma-separated
max_clique = bron_kerbosch_pivot(set(), set(network.keys()), set())
password = ','.join(sorted(max_clique))
print(f'Part Two: {password}')
