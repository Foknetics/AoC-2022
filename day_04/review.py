PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    section_pairs = f.readlines()

section_pairs = [pair.strip() for pair in section_pairs]

def convert_to_set(assignment):
    start, end = assignment.split('-')
    return set([section for section in range(int(start), int(end)+1)])

pairs_to_review = 0

for pair in section_pairs:
    elf_a, elf_b = pair.split(',')
    elf_a = convert_to_set(elf_a)
    elf_b = convert_to_set(elf_b)
    if len(elf_a.intersection(elf_b)) or len(elf_b.intersection(elf_a)):
        pairs_to_review += 1

print(f'There are {pairs_to_review} pairs where one assignment is fully contained within the other.')
