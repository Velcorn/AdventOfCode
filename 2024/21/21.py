# Read input as list of strings
with open('21_example.txt') as f:
    codes = [line.strip() for line in f]

# Keypads of the robots and the player
r1_numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [' ', '0', 'A']]
r2_dpad = [[' ', '^', 'A'], ['<', 'v', '>']]
r3_dpad = [[' ', '^', 'A'], ['<', 'v', '>']]
my_dpad = [[' ', '^', 'A'], ['<', 'v', '>']]

# Part One: What is the sum of the complexities of the five codes on your list?
complexitites = [int(code.lstrip('0').rstrip('A')) for code in codes]
print(f'Part One: {complexitites}')
