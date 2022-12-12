PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    rucksacks = f.readlines()


def priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


total_priority = 0

for rucksack in rucksacks:
    compartment_1 = rucksack[:len(rucksack)//2]
    compartment_2 = rucksack[len(rucksack)//2:]
    for item in compartment_1:
        if item in compartment_2:
            total_priority += priority(item)
            break
print(f'Sum of priorities of duplicate items: {total_priority}')
