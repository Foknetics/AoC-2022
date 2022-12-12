PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    rucksacks = f.readlines()

rucksacks = [sack.strip() for sack in rucksacks]


def priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


total_priority = 0

groups = [rucksacks[group: group+3] for group in range(0, len(rucksacks), 3)]

for group in groups:
    sack_1, sack_2, sack_3 = group
    for item in sack_1:
        if item in sack_2 and item in sack_3:
            total_priority += priority(item)
            break

print(f'Sum of priorities of badges: {total_priority}')
