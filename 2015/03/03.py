# Read input as string
with open("03_input.txt", "r") as f:
	directions = f.read().strip()

moves = {
	'^': (0, 1),
	'v': (0, -1),
	'<': (-1, 0),
	'>': (1, 0)
}

# Part One: The number of houses that receive at least one present from Santa
houses = 1
pos = (0, 0)
visited = {pos}
for direction in directions:
	dx, dy = moves[direction]
	pos = (pos[0] + dx, pos[1] + dy)
	if pos not in visited:
		visited.add(pos)
		houses += 1
print(f"Part One: {houses}")

# Part Two: The number of houses that receives at least one present from (Robo-)Santa
houses = 1
spos = (0, 0)
rpos = (0, 0)
visited = {(0, 0)}
for i, direction in enumerate(directions):
	dx, dy = moves[direction]
	if i % 2 == 0:
		pos = spos
	else:
		pos = rpos
	pos = (pos[0] + dx, pos[1] + dy)
	if pos not in visited:
		visited.add(pos)
		houses += 1
	if i % 2 == 0:
		spos = pos
	else:
		rpos = pos
print(f"Part Two: {houses}")
