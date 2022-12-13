PUZZLE_INPUT = 'test_input.txt'

with open(PUZZLE_INPUT) as f:
    rope_movement_data = f.read().splitlines()

def adjacent_coords(coord):
    coords = []
    for y_offset in range(1, -2, -1):
        for x_offset in range(-1, 2):
            coords.append((coord[0] + x_offset, coord[1] + y_offset))
    return coords

head_x, head_y = (0, 0)
tail_x, tail_y = (0, 0)

tail_locations = [(0, 0)]

for move in rope_movement_data:
    if move[0] == 'L':
        head_x -= 1
    elif move[0] == 'R':
        head_x += 1
    elif move[0] == 'U':
        head_y += 1
    elif move[0] == 'D':
        head_y -= 1

    adjacent_to_head = adjacent_coords((head_x, head_y))

    print(adjacent_to_head)
    print((tail_x, tail_y))
    print((tail_x, tail_y) not in adjacent_to_head)

    if (tail_x, tail_y) not in adjacent_to_head:
        print('tail needs to move')
        for coord in adjacent_coords((tail_x, tail_y)):
            if coord in adjacent_to_head:
                tail_x, tail_y = coord
                if coord not in tail_locations:
                    tail_locations.append(coord)

print(f'Tail visited {len(tail_locations)} locations.')
