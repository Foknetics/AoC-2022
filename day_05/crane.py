PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    input_lines = f.read().splitlines()

crate_map = {}
instruction_start_line = 0

for line_index, line in enumerate(input_lines):
    if line[1] == '1':
        instruction_start_line = line_index + 1
        break

    for index, char in enumerate(line):
        if (index - 1) % 4 == 0 and char != ' ':
            column = ((index - 1) // 4) + 1
            try:
                crate_map[column].insert(0, char)
            except KeyError:
                crate_map[column] = [char]

for instruction in input_lines[instruction_start_line+1:]:
    _, crate_count, _, start_col, _, end_col = instruction.split(' ')
    crate_count = int(crate_count)
    start_col = int(start_col)
    end_col = int(end_col)

    for _ in range(crate_count):
        pick_up_crate = crate_map[start_col].pop()
        crate_map[end_col].append(pick_up_crate)

top_crates = ''
for key in sorted(list(crate_map.keys())):
    top_crates += crate_map[key][-1]

print(f'The top crate in each stack is: {top_crates}')
