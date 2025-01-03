# Read input as list of ints
with open('22_input.txt') as f:
    secret_numbers = [int(x) for x in f.read().split()]

# Process the evolutions of the secret numbers
final_secret_numbers = []
sequences = {}
for sn in secret_numbers:
    seqs = {}
    changes = {}
    price = sn % 10
    for i in range(2000):
        # Step 1: Multiply by 64, calculate bitwise XOR with result and secret number
        result = sn * 64
        sn = result ^ sn
        sn %= 16777216
        # Step 2: Divide by 32, calculate bitwise XOR with result and secret number, modulo 16777216
        result = sn // 32
        sn = result ^ sn
        sn %= 16777216
        # Step 3: Multiply by 2048, calculate bitwise XOR with result and secret number, modulo 16777216
        result = sn * 2048
        sn = result ^ sn
        sn %= 16777216
        # Get the price (last digit) and the change compared to the previous price
        new_price = sn % 10
        change = new_price - price
        price = new_price
        changes[i] = change
        # Add the 4 last changes and current price to the sequences
        if i >= 3:
            seq = (changes[i - 3], changes[i - 2], changes[i - 1], changes[i])
            if seq not in seqs:
                seqs[seq] = price
    final_secret_numbers.append(sn)
    for seq, price in seqs.items():
        if seq not in sequences:
            sequences[seq] = price
        else:
            sequences[seq] += price

# Part One: Sum of the 2000th secret number generated by each buyer
print(f'Part One: {sum(final_secret_numbers)}')

# Part Two: Most bananas one can get
print(f'Part Two: {max(sequences.values())}')
