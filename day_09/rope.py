import math

PUZZLE_INPUT = 'input.txt'

with open(PUZZLE_INPUT) as f:
    rope_movement_data = f.read().splitlines()


def adjacent_coords(coord):
    coords = []
    for y_offset in range(1, -2, -1):
        for x_offset in range(-1, 2):
            coords.append((coord[0] + x_offset, coord[1] + y_offset))
    return coords


def distance(coord_1, coord_2):
    x1, y1 = coord_1
    x2, y2 = coord_2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


head_x, head_y = (0, 0)
tail_x, tail_y = (0, 0)

tail_locations = [(0, 0)]

for move in rope_movement_data:
    direction, steps = move.split(' ')
    steps = int(steps)
    for steps in range(0, steps):
        if direction == 'L':
            head_x -= 1
        elif direction == 'R':
            head_x += 1
        elif direction == 'U':
            head_y += 1
        elif direction == 'D':
            head_y -= 1

        adjacent_to_head = adjacent_coords((head_x, head_y))

        if (tail_x, tail_y) not in adjacent_to_head:
            potential_moves = adjacent_coords((tail_x, tail_y))
            viable_moves = list(set(adjacent_to_head).intersection(set(potential_moves)))
            viable_moves = sorted(viable_moves, key=lambda move: distance(move, (head_x, head_y)))
            tail_x, tail_y = viable_moves[0]
            tail_locations.append(viable_moves[0])

tail_locations = list(set(tail_locations))
print(f'Tail visited {len(tail_locations)} locations.')
