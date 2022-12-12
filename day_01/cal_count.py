PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    lines = f.readlines()

elves = {}
elf = 0

for line in lines:
    if line == '\n':
        elf += 1
        continue
    try:
        elves[elf] += int(line)
    except KeyError:
        elves[elf] = int(line)

max_elf = sorted(elves.items(), key=lambda elf: elf[1])[-1][1]
print(f'The elf carrying the most calories is carrying {max_elf} calories.')


max_three_elves = sum([elf[1] for elf in sorted(elves.items(), key=lambda elf: elf[1])[-3:]])
print(f'The three elves carrying the most calories are carrying {max_three_elves} calories.')
